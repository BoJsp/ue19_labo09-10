# conding utf-8
import requests
# import json

response = requests.get("https://www.punapi.rest/api/pun")
test = response.json()
print("La blague :", test["pun"])
