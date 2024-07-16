from flask import Flask, render_template_string, request

app = Flask(__name__)

# Template string containing HTML and embedded CSS
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOI Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            text-align: center;
            width: 300px;
        }

        form {
            margin-bottom: 20px;
        }

        form label {
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }

        form input[type="text"] {
            width: calc(100% - 16px);
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        form button {
            width: 100%;
            padding: 10px 0;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        form button:hover {
            background-color: #0056b3;
        }

        .result {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        .result h2 {
            margin-top: 0;
            color: #333;
        }

        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>SOI Calculator</h1>
        
        <form action="{{ url_for('calculate_soi') }}" method="post">
            <label for="engine_rpm">Engine RPM:</label>
            <input type="text" id="engine_rpm" name="engine_rpm"><br>
            
            <label for="injection_mg_cyc">Injection mg/cyc:</label>
            <input type="text" id="injection_mg_cyc" name="injection_mg_cyc"><br>
            
            <button type="submit">Calculate</button>
        </form>

        {% if soi_value is defined %}
            <div class="result">
                <h2>SOI Value:</h2>
                <p>{{ soi_value }}</p>
            </div>
        {% elif error %}
            <div class="error">{{ error }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            engine_rpm = float(request.form['engine_rpm'])
            injection_mg_cyc = float(request.form['injection_mg_cyc'])
            
            # Perform SOI calculation (replace with your calculation logic)
            soi_value = int((engine_rpm / 2) * (injection_mg_cyc / 166666.67) / 0.023438)

            return render_template_string(template, soi_value=soi_value)
        
        except ValueError:
            error = "Invalid input. Please enter valid numbers."
            return render_template_string(template, error=error)
    
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)
