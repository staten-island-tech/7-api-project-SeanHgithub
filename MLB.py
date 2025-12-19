import requests
import tkinter as tk
window = tk.Tk()
window.title("Word Search")
window.geometry("1000x500")

label = tk.Label(
    window,
    text="Word Search",
    bg="lightblue",
    fg="black",
    font=("Arial", 14),
    padx=10,
    pady=10
)


label.pack(
    side="top",
    pady=10
)

entry = tk.Entry(window)
entry.pack(pady=10)

def getword():
    search = entry.get()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{search.lower()}")
    if response.status_code != 200:
        window.title("Error Fetching Data!")
        return None
    data = response.json()
    window.title("Word Found!")
    word =  {
        "word": data[0]["word"],
        "definitions": [
         d["definition"]
         for m in data[0]["meanings"]
         for d in m["definitions"]
         ]
    }
    organize_word = [
        (f"{key.title()}: {value}")
        for key, value in word.items()
    ]
    output = tk.Label(
        window,
        text="\n".join(organize_word),
        bg="lightblue",
        fg="black",
        font=("Arial", 14),
        padx=10,
        pady=10,
        wraplength=900,
        justify="left"
    )
    output.pack()
button = tk.Button(window, text="Submit", command=getword)
button.pack()

window.mainloop()

