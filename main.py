import requests
from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.title("Chuck Norris Joke")
window.geometry("400x400")


def chuck_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        data = response.json()
        return data["value"]
    except:
        messagebox.showerror("You're Offline", "Check your connection")


joke = Message(window, text=chuck_joke())
joke.pack()


def get_joke():
    joke.config(text=chuck_joke())


joke_button = Button(window, text="Joke", command=get_joke)
joke_button.pack()


window.mainloop()
