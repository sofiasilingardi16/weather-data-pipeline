# Weather Data Pipeline with Python and PostgreSQL

This project is a simple ETL pipeline that collects hourly weather forecast data from the Open-Meteo API, transforms the raw JSON response into clean tabular data, and loads it into a PostgreSQL database running inside a Docker container.

## Tech Stack

- Python
- Pandas
- Requests
- PostgreSQL
- Docker
- Psycopg

## Pipeline Overview

1. Extract weather forecast data from Open-Meteo API
2. Transform JSON data into a structured DataFrame
3. Clean missing values and remove duplicates
4. Load the data into PostgreSQL
5. Use upsert logic to avoid duplicate records

## Cities Included

- Bologna
- Milan
- Rome

## How to Run

Start PostgreSQL:

```bash
docker compose up -d

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python3 src/main.py
```

## Database Table

The main table is `weather_hourly`, containing:

- location name
- latitude
- longitude
- forecast timestamp
- temperature
- relative humidity
- wind speed
- loading timestamp

## Key Data Engineering Concepts

- API data ingestion
- JSON normalization
- Data cleaning
- PostgreSQL storage
- Dockerized database
- Idempotent loading with `ON CONFLICT`


