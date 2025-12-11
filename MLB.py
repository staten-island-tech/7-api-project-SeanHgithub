import requests

def getword(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    
    data = response.json()
    return {
        "word": data[0]["word"],
        "definitions": [
        d["definition"]
        for m in data[0]["meanings"]
        for d in m["definitions"]
        ]
    }
word = getword("hello")

for key, value in word.items():
    print(f"{key.title()}: {value}")