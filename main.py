from requests.api import request
from config import app_id, app_key, sheetys_endpoint, auth
import requests
from datetime import datetime

user_input = input("Tell me which exercises you did: ")

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
  "x-app-id": app_id,
  "x-app-key": app_key,
  "Content-Type": "application/json"
}

request_body = {
  "query": user_input
}

response = requests.post(url=nutritionix_endpoint, json=request_body,headers=headers)
response.raise_for_status()
workout_data = response.json()["exercises"]

sheetys_headers = {
  "Authorization": auth,
  "Content-Type": "application/json"
}

for work_out in workout_data:
  work_out_info = {
    "workout": {
      "date": datetime.now().strftime("%D"),
      "time": datetime.now().strftime("%H:%M:%S"),
      "exercise": work_out["name"].title(),
      "duration": work_out["duration_min"],
      "calories": work_out["nf_calories"]
    }
  }
  requests.post(url=sheetys_endpoint, json=work_out_info, headers=sheetys_headers)
  
