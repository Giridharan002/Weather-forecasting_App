import requests

apikey = "04c1ae798b5150ccc3d75e60f5e13b26"
weatherDataEl = None  # Assuming weatherDataEl is an HTML element in the original code
cityinputEl = None  # Assuming cityinputEl is an HTML element in the original code

def getWeatherData(cityValue):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cityValue}&appid={apikey}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = round(data['main']['temp'])
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']

        details = [
            f"Feels like: {round(data['main']['feels_like'])}",
            f"Humidity: {data['main']['humidity']}%",
            f"Wind speed: {data['wind']['speed']}m/s"
        ]

        # Assuming the following lines of code modify the DOM
        weatherDataEl.querySelector(".icon").innerHTML = f'<img src="http://openweathermap.org/img/wn/{icon}.png" alt="Weather Icon">'
        weatherDataEl.querySelector(".temperature").textContent = f"{temperature}°C"
        weatherDataEl.querySelector(".description").textContent = description
        weatherDataEl.querySelector(".details").innerHTML = ''.join([f"<div>{detail}</div>" for detail in details])
    
    except requests.exceptions.RequestException as error:
        # Assuming the following lines of code modify the DOM
        weatherDataEl.querySelector(".icon").innerHTML = ""
        weatherDataEl.querySelector(".temperature").textContent = ""
        weatherDataEl.querySelector(".description").textContent = "Error happened, please try again later!"
        weatherDataEl.querySelector(".details").innerHTML = ""

def handle_form_submit(event):
    event.preventDefault()
    cityValue = cityinputEl.value
    getWeatherData(cityValue)

formEl = None  # Assuming formEl is an HTML element in the original code
formEl.addEventListener("submit", handle_form_submit)
