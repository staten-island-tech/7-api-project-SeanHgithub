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

def show_def():
    def getword(word):
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}")
        if response.status_code != 200:
            window.title("Error Fetching Data!")
            return None
        data = response.json()
        window.title("Word Found!")
        word_info =  
                "word": data[0]["word"],
                "definitions": [
                d["definition"]
                for m in data[0]["meanings"]
                for d in m["definitions"]
                ]
            }
        output.pack()
        text = entry.get()
        word = getword(text)
    
    


button = tk.Button(window, text="Submit", command=show_def)
button.pack()

window.mainloop()



""" for key, value in word.items():
    print(f"{key.title()}: {value}") """

