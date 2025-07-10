import pywhatkit
import webbrowser as web
import speech_recognition as sr
import wikipedia as googleScrap
import pyttsx3
import openai
import os
API_KEY = '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'

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def g_search(prompt):
    prompt = prompt.replace("google search", "")
    prompt = prompt.replace("search", "")
    prompt = prompt.replace("google", "")
    speak("This is what i Found on Internet")
    pywhatkit.search(prompt)
    try:
        result = googleScrap.summary(prompt, 4)
        return result
    except Exception as e:
        result = "No Speakable Data Available"
        return result

def openqu(term):
    prompt = term
    os.environ['OPENAI_Key'] = API_KEY
    openai.api_key = os.environ['OPENAI_Key']
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=50, temperature=0.7)
    ans = (response['choices'][0]['text'])
    return ans

def Youtube(term):
    result = f"https://www.youtube.com/results?search_query={term}"
    # print(result)
    web.open(result)
    # speak("This is what I found")

def Youtube_lat(term):
    # result = f"https://www.youtube.com/results?search_query={term}"
    # print(result)
    pywhatkit.playonyt(term)
