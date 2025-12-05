
import requests

url = "http://developer.marvel.com"
headers = {
    "Content-Type": "application/json"
}

response = requests.get(url)
data = response.json()
print(data)
