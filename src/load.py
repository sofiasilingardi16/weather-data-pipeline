import psycopg

def load_to_postgres(df):
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="weather_db",
        user="weather_user",
        password="weather_pass"
    )

    cur = conn.cursor()

    insert_query = """
    INSERT INTO weather_hourly (
        location_name,
        latitude,
        longitude,
        forecast_time,
        temperature_2m,
        relative_humidity_2m,
        wind_speed_10m
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (location_name, forecast_time)
    DO UPDATE SET
        temperature_2m = EXCLUDED.temperature_2m,
        relative_humidity_2m = EXCLUDED.relative_humidity_2m,
        wind_speed_10m = EXCLUDED.wind_speed_10m,
        loaded_at = CURRENT_TIMESTAMP;
    """

    for _, row in df.iterrows():
        cur.execute(insert_query, (
            row["location_name"],
            row["latitude"],
            row["longitude"],
            row["forecast_time"],
            row["temperature_2m"],
            row["relative_humidity_2m"],
            row["wind_speed_10m"]
        ))

    conn.commit()
    cur.close()
    conn.close()