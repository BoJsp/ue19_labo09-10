# conding utf-8
import requests
# import json

# process
response = requests.get("https://www.punapi.rest/api/pun")
test = response.json()
print("La blague :", test["pun"])
