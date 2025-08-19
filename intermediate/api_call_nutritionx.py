import requests
import datetime

# https://docx.syndigo.com/developers/docs/nutritionix-api-guide
host_domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"

nutritionx_headers = {
    "x-app-id": "<add nutritionx app id>",
    "x-app-key": "<add nutritionx app key>"
}

nutritionx_body = {
    "query": "2 hours easy run"
}

nutritionx_response = requests.post(
    url=host_domain + endpoint,
    headers=nutritionx_headers,
    json=nutritionx_body
)
nutritionx_response.raise_for_status()
json = nutritionx_response.json()["exercises"][0]

user_input = json["user_input"]
duration_min = json["duration_min"]
calories = json["nf_calories"]
date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")

# https://sheety.co/docs/authentication.html
sheety_project_id = "add sheety project id"
sheety_endpoint = f"https://api.sheety.co/{sheety_project_id}/myWorkouts/workouts"

sheety_body = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": user_input,
        "duration": duration_min,
        "calories": calories
    }
}

sheety_headers = {
    "Authorization": "add sheety bearer token auth key"
}

sheety_response = requests.post(
    url=sheety_endpoint,
    json=sheety_body,
    headers=sheety_headers
)
sheety_response.raise_for_status()
print(sheety_response.text)