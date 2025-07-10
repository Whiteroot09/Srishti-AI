import speech_recognition as sr
import pyttsx3
import tkinter as tk

def speak(text, head_lable, textarea, bottom_lable):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 180-200)
    head_lable.config(fg="#7B241C")
    textarea.tag_configure("left", justify='left')
    textarea.tag_configure("colored1", foreground='#7B241C')
    textarea.tag_configure("box1", background="#AEB6BF", borderwidth=1, relief="solid")
    textarea.insert(tk.END, f"SRIshti Said : ", "left colored1 box1")
    textarea.insert(tk.END, f"{text}\n", "left")
    textarea.see(tk.END)
    bottom_lable.config(text="Speak...", bg="#7B241C", fg="white")
    print(f"SRIshti Said : {text}")
    engine.say(text)
    engine.runAndWait()

def min_speak(text, head_lable):
    if type(text) is list:
        text = " ".join(text)
    else:
        text = text
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    engine.setProperty('rate', 180-200)
    head_lable.config(fg="#7B241C")
    print(f"SRIshti Said : {text}")
    engine.say(text)
    engine.runAndWait()

def takeCommand(head_lable, textarea, bottom_lable):
    r = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            head_lable.config(fg="#117864")
            bottom_lable.config(text="Listening...", bg="#117864", fg="white")
            print('Listening...')
            audio = r.listen(mic, phrase_time_limit=4)
            bottom_lable.config(text="Recognizing...", bg="#82E0AA", fg="white")
            head_lable.config(fg="#82E0AA")
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User Said: {query}")
            textarea.tag_configure("right", justify='right')
            textarea.tag_configure("colored2", foreground='#117864')
            textarea.tag_configure("box2", background="#AEB6BF", borderwidth=1, relief="solid")
            textarea.insert(tk.END, f"{query}", "right")
            textarea.insert(tk.END, f" : User Said\n", "right colored2 box2")
            textarea.see(tk.END)
            query = str(query).lower()
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service; check your internet connection")
        return ""
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return ""
    return query
