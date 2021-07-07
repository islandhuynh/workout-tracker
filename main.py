from requests.api import request
from config import app_id, app_key, sheetys_endpoint
import requests

text = "I ran 3 miles and walked 2 miles"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
  "x-app-id": app_id,
  "x-app-key": app_key,
  "Content-Type": "application/json"
}

request_body = {
  "query": "I ran 3 miles and walked 2 miles",
}

response = requests.post(url=nutritionix_endpoint, json=request_body,headers=headers)
print(response.json())