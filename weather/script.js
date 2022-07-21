async function getData(city) {
  const query = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=9bac5117b64a7764fb9a90466bf4f19f`, {mode:'cors'}
  );
  const response = await query.json();
  const data = await response;
  const weather = data.weather[0].main;
  document.querySelector("#weather").textContent = data.weather[0].main;
  document.querySelector("#city").textContent = data.name;
  document.querySelector("#temperature").textContent =
    Math.floor(data.main.temp - 273.15) + "°C";
  document.querySelector("#feels").textContent =
    Math.floor(data.main.feels_like - 273.15) + "°C";
  document.querySelector("#humidity").textContent = data.main.humidity + "%";
  document.querySelector("#wind").textContent =
    Math.floor(data.wind.speed) + "m/s";
  return data;
}

getData("london");

const Element = document.querySelector("form")
Element.addEventListener("submit", (event) => {
  event.preventDefault();
  getData(Element.elements.search.value);
});
