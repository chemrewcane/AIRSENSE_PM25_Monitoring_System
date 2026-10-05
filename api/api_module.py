import requests

from config.config_module import (
    AIR_QUALITY_API_URL,
    PM25_BREAKPOINTS,
    UM_MATINA_LATITUDE,
    UM_MATINA_LONGITUDE,
)

def fetch_pm25_from_api():
    params = {
        "latitude": UM_MATINA_LATITUDE,
        "longitude": UM_MATINA_LONGITUDE,
        "current": "pm2_5",
        "timezone": "Asia/Manila",
    }

    response = requests.get(
        AIR_QUALITY_API_URL,
        params=params,
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()
    pm25_value = data["current"]["pm2_5"]

    if pm25_value is None:
        raise ValueError("API returned no PM2.5 data at this time.")

    return float(pm25_value)

def classify_pm25(pm25_value):
    for low, high, category, advisory in PM25_BREAKPOINTS:
        if low <= pm25_value <= high:
            return category, advisory

    if pm25_value < 0:
        raise ValueError("PM2.5 value cannot be negative.")

    return (
        "Hazardous",
        "Health warning of emergency conditions.",
    )