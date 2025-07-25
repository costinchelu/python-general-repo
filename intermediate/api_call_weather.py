import os
import requests


OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_URL = "https://api.openweathermap.org/data/2.5/forecast"
NO_OF_ENTRIES = 4
GET_CALL_PARAMS = {
    "lat": "44.4268",
    "lon": "-26.1025",
    "units": "metric",
    "cnt": NO_OF_ENTRIES,
    "appid": OPEN_WEATHER_API_KEY
}

response = requests.get(url=OPEN_WEATHER_URL, params=GET_CALL_PARAMS)
response.raise_for_status()
response_data = response.json()

rain_intervals = []
intervals = response_data["list"]
for interval in intervals:
    if interval["weather"][0]["id"] < 700:
        rain_intervals.append(interval["dt_txt"])

print(f"It will rain on: {rain_intervals}")
