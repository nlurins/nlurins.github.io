async function getData(city) {
  const query = await fetch(
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=9bac5117b64a7764fb9a90466bf4f19f`, {mode:'cors'}
  );
  const response = await query.json();
  const data = await response;
  const weather = data.weather[0].main;
  console.log(data);
  document.querySelector("#weather").textContent = data.weather[0].main;
  document.querySelector("#city").textContent = data.name;
  document.querySelector("#temperature").textContent =
    Math.floor(data.main.temp - 273.15) + "°C";
  document.querySelector("#feels").textContent =
    Math.floor(data.main.feels_like - 273.15) + "°C";
  document.querySelector("#humidity").textContent = data.main.humidity + "%";
  document.querySelector("#wind").textContent =
    Math.floor(data.wind.speed) + "m/s";
  console.log(window.location.search);
  return data;
}

getData("london");
input();

async function getNew() {
  const str = await window.location.search;
  const newstr = await str.replace("?search=", "");
  getData(newstr);
  console.log(newstr);
}

function input(){
  const inputbox = document.querySelector('form');
  inputbox.addEventListener('submit', e => {
    e.preventDefault();
    getNew(inputbox.value);
  });
}