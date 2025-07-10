import pyttsx3
import tkinter as tk
import urllib.request as urec

def online(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180-200)
    print(f"SRIshti Said : {text}")
    engine.say(text)
    engine.runAndWait()

def check_internet_connection():
    try:
        host = "https://www.google.com/"
        urec.urlopen(host)
        return True
    except Exception as e:
        return False

def check_internet_gui():
    root = tk.Tk()
    root.title("Internet Connection Checker - Online")
    root.geometry("300x100")

    label = tk.Label(root, text="Checking internet connection...")
    label.pack(pady=20)
    root.title("Internet Connection Checker - Offline")  # Update the title bar
    label.config(text="Internet is not connected.")

    root.mainloop()
