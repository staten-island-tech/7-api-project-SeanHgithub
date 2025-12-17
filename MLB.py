import requests
import tkinter as tk
window = tk.Tk()
window.title("Word Search")
window.geometry("1000x500")

label = tk.Label(
    window,
    text="Hello, Tkinter!",
    bg="lightblue",
    fg="black",
    font=("Arial", 14),
    padx=10
    pady=10
)

label.pack(
    side="top",
    pady=10
)

button = tk.Button(
    window,
    text="Click Me",
    command=lambda: print("Button clicked!")
)

button.pack(
    side="bottom",
    pady=10
)
window.mainloop()
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
word = getword("banana")

for key, value in word.items():
    print(f"{key.title()}: {value}")

