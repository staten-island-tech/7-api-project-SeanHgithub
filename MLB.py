import requests

url = "https://marvel-snap-api.p.rapidapi.com/api/get-all-cards"

querystring = {"page":"1"}

headers = {
	"x-rapidapi-key": "fb2044aa18msh62f0ab07b46ac36p19f523jsn9f224fb4edd3",
	"x-rapidapi-host": "marvel-snap-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
