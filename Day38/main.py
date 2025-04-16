import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()  # Load from .env

NUTRITIONIX_ID = os.getenv("NUTRITIONIX_ID")
NUTRITIONIX_KEY = os.getenv("NUTRITIONIX_KEY")
GENDER = os.getenv("GENDER")
WEIGHT = os.getenv("WEIGHT")
HEIGHT = os.getenv("HEIGHT")
AGE = os.getenv("AGE")
NUTRITIONIX_ENDPOINT = os.getenv("NUTRITIONIX_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

REQUEST_HEADERS = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_KEY,
}

# Get the exercise data from the user
exercise_text = input("Tell me which exercises you did: ")

querry_json = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=REQUEST_HEADERS, json=querry_json, verify=False)
response.raise_for_status()
exercise_data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in exercise_data["exercises"]:
    
    exercise_name = exercise["name"].title()
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]

    sheety_headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
    }

    sheety_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data, headers=sheety_headers, verify=False)
    sheety_response.raise_for_status()
