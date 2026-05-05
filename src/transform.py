import pandas as pd

def transform_data(data, city):
    hourly = data["hourly"]

    df = pd.DataFrame({
        "location_name": city["name"],
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "forecast_time": hourly["time"],
        "temperature_2m": hourly["temperature_2m"],
        "relative_humidity_2m": hourly["relative_humidity_2m"],
        "wind_speed_10m": hourly["wind_speed_10m"]
    })

    df["forecast_time"] = pd.to_datetime(df["forecast_time"])

    df = df.drop_duplicates(subset=["location_name", "forecast_time"])
    df = df.dropna(subset=["temperature_2m"])

    return df