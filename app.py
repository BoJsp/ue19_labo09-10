# conding utf-8
import requests

url = "https://www.punapi.rest/randompun"
response = requests.get(url)
data = response.json()
print("La blague:", data['content'])
