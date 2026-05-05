from extract import get_weather_data
from transform import transform_data
from load import load_to_postgres
def run_pipeline():
    cities = [
        {"name": "Bologna", "latitude": 44.4949, "longitude": 11.3426, "timezone": "Europe/Rome"},
        {"name": "Milan", "latitude": 45.4642, "longitude": 9.1900, "timezone": "Europe/Rome"},
        {"name": "Rome", "latitude": 41.9028, "longitude": 12.4964, "timezone": "Europe/Rome"}
    ]

    for city in cities:
        print(f"Processing {city['name']}...")

        raw_data = get_weather_data(city)
        df = transform_data(raw_data, city)
        load_to_postgres(df)

    print("Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()