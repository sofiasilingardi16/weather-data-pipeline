import requests

def get_weather_data(city):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": city["timezone"]
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()