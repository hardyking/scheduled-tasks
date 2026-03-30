import requests
from datetime import datetime, timezone, timedelta
import os

BARK_KEY = os.environ.get("BARK_KEY")
OWM_APP_ID = os.environ.get("OWM_APP_ID")

parameters = {
    "appid": OWM_APP_ID,
    "lat": 31.121378,
    "lon": 121.514857,
    "cnt": 4
}

def send_bark():
    utc_plus_8 = timezone(timedelta(hours=8))
    now_utc8 = datetime.now(utc_plus_8)
    date = now_utc8.date().strftime("%Y-%m-%d")
    content = "今天会下雨"
    access_url = f"https://api.day.app/{BARK_KEY}/{date}/{content}"
    requests.get(access_url)

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data: list = response.json()["list"]

rainy_day = False

for three_hour_weather_data in weather_data: #dict in list
    if rainy_day:
        break
    for three_hour_weather in three_hour_weather_data["weather"]: #dict in list
        if three_hour_weather["id"] < 700:
            send_bark()
            rainy_day = True
            break
