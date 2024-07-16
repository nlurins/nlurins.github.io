import struct
import numpy as np
import json
from scipy.interpolate import RegularGridInterpolator
from flask import Flask, request, jsonify

app = Flask(__name__)

class BoschECUMapExtractor:
    def __init__(self, file_path, endianness='big'):
        self.file_path = file_path
        self.endianness = endianness
        self.values = self.read_16bit_endian()

    def read_16bit_endian(self):
        with open(self.file_path, "rb") as f:
            data = f.read()
        # Determine the format string based on endianness
        num_values = len(data) // 2
        if self.endianness == 'big':
            values = struct.unpack(f">{num_values}H", data)
        else:
            values = struct.unpack(f"<{num_values}H", data)
        return values

    def extract_axes(self, start_index):
        y_length = self.values[start_index]
        x_length = self.values[start_index + 1]
        y_axis = self.values[start_index + 2: start_index + 2 + y_length]
        x_axis = self.values[start_index + 2 + y_length: start_index + 2 + y_length + x_length]
        new_start_index = start_index + 2 + y_length + x_length
        return y_axis, x_axis, new_start_index

    def extract_map_with_axes(self, axis_length_address):
        start_index = axis_length_address // 2  # Convert address to index

        # Extract axes
        y_axis, x_axis, start_index = self.extract_axes(start_index)

        # Calculate the number of rows and columns from the axes lengths
        num_rows = len(y_axis)
        num_columns = len(x_axis)

        # Extract map data
        map_data = []
        for row in range(num_rows):
            row_data = self.values[start_index:start_index + num_columns]
            if len(row_data) != num_columns:
                raise ValueError(
                    f"Inconsistent number of columns at row {row}: expected {num_columns}, got {len(row_data)}")
            map_data.append(row_data)
            start_index += num_columns

        return {
            "x_axis": np.array(x_axis).tolist(),
            "y_axis": np.array(y_axis).tolist(),
            "map": np.array(map_data).tolist()
        }

class BoschECUInterpolator:
    def __init__(self, extracted_maps):
        self.extracted_maps = extracted_maps

    def interpolate_fuel_pressure(self, rpm, mg_cyc):
        rail_map = self.extracted_maps["rail_fuel_pressure_map"]
        rpm_axis = np.array(rail_map['y_axis'])
        mg_cyc_axis = np.array(rail_map['x_axis'])
        pressure_map = np.array(rail_map['map'])

        # Ensure rpm and mg_cyc are within bounds
        rpm = np.clip(rpm, rpm_axis.min(), rpm_axis.max())
        mg_cyc = np.clip(mg_cyc, mg_cyc_axis.min(), mg_cyc_axis.max())

        interp_func = RegularGridInterpolator((rpm_axis, mg_cyc_axis), pressure_map)
        return interp_func((rpm, mg_cyc))

    def interpolate_duration(self, pressure, mg_cyc):
        duration_map = self.extracted_maps["duration_of_injection_map"]
        pressure_axis = np.array(duration_map['y_axis'])
        mg_cyc_axis = np.array(duration_map['x_axis'])
        duration_map_data = np.array(duration_map['map'])

        # Ensure pressure and mg_cyc are within bounds
        pressure = np.clip(pressure, pressure_axis.min(), pressure_axis.max())
        mg_cyc = np.clip(mg_cyc, mg_cyc_axis.min(), mg_cyc_axis.max())

        interp_func = RegularGridInterpolator((pressure_axis, mg_cyc_axis), duration_map_data)
        return interp_func((pressure, mg_cyc))

def create_new_map(interpolator, rpm_axis, mg_cyc_axis):
    num_rows = len(rpm_axis)
    num_columns = len(mg_cyc_axis)

    # Initialize an empty SOI map
    soi_map = np.zeros((num_rows, num_columns), dtype=int)

    for i, rpm in enumerate(rpm_axis):
        for j, mg_cyc in enumerate(mg_cyc_axis):
            # Interpolate fuel pressure from the rail map
            fuel_pressure = interpolator.interpolate_fuel_pressure(rpm, mg_cyc)

            # Interpolate duration of injection from the duration map
            duration_injection = interpolator.interpolate_duration(fuel_pressure, mg_cyc)

            # Calculate SOI value using the formula: int((rpm * duration_injection / 166666.67) / 0.023438)
            soi_map[i, j] = int(((rpm / 2) * duration_injection / 166666.67) / 0.023438)

    new_map = {
        "x_axis": mg_cyc_axis.tolist(),
        "y_axis": rpm_axis.tolist(),
        "map": soi_map.tolist()
    }

    return new_map

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    endianness = request.form['endianness']
    rpm_axis = np.array([int(x) for x in request.form['rpm_axis'].split()])
    mg_cyc_axis = np.array([int(x) for x in request.form['mg_cyc_axis'].split()])
    duration_address = int(request.form['duration_address'], 16)
    rail_pressure_address = int(request.form['rail_pressure_address'], 16)

    file.save('uploaded_file.bin')

    extractor = BoschECUMapExtractor('uploaded_file.bin', endianness)
    
    extracted_maps = {
        "duration_of_injection_map": extractor.extract_map_with_axes(duration_address),
        "rail_fuel_pressure_map": extractor.extract_map_with_axes(rail_pressure_address)
    }

    interpolator = BoschECUInterpolator(extracted_maps)
    new_map = create_new_map(interpolator, rpm_axis, mg_cyc_axis)

    return jsonify(new_map)

if __name__ == "__main__":
    app.run(debug=True)
