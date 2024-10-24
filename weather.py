import requests

# API settings
api_key = "a42a69750078c5ff8c678f0fcf5e5bf0"
current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

def weather(City):
    current_url = f"{current_weather_url}?q={City}&appid={api_key}&units=metric"
    current_response = requests.get(current_url)
    current_weather = current_response.json()

    temp = current_weather["main"]["temp"]
    namlik = current_weather["main"]["humidity"]
    wind = current_weather["wind"]["speed"]


    return f"Ob-havo : {temp}°\nNamlik: {namlik} % \nShamol: sekundiga {wind} m/s"

