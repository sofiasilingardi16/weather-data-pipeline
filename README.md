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


