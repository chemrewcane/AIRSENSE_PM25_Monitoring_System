UM_MATINA_LATITUDE = 7.066998
UM_MATINA_LONGITUDE = 125.597873

AIR_QUALITY_API_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
)

CAMPUS_LOCATIONS = [
    "GET Building",
    "BE Building",
    "PS Building",
    "DPT Building",
    "BED Building",
    "FEA Building",
    "CTE Building",
    "Innovation Complex",
    "UM Gym / UM Clinic",
    "Oval Track",
    "UM Library",
    "UM Cafeteria",
    "Matina Gate",
    "Maa Gate",
]

PM25_BREAKPOINTS = [
    (0.0, 12.0, "Good", "Air quality is satisfactory."),
    (12.1, 35.4, "Moderate", "Air quality is ok."),
    (
        35.5,
        55.4,
        "Unhealthy for Sensitive People",
        "Sensitive groups may experience health effects.",
    ),
    (
        55.5,
        150.4,
        "Unhealthy",
        "Everyone may begin to experience health effects.",
    ),
    (
        150.5,
        250.4,
        "Very Unhealthy",
        "Everyone may experience more serious health effects.",
    ),
    (
        250.5,
        500.4,
        "Hazardous",
        "Health warning of emergency conditions.",
    ),
]