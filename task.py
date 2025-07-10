import time
from database_json_ROK import login
import openai
import os
import pywhatkit
import wikipedia
import requests
import webbrowser as web
from test import takeCommand, speak
from prediction import hotword
import datetime
from plyer import notification
from news import news

#############TASK############
############Non Input Functions###########
def exit_open(root, head_lable, textarea, bottom_lable):
    hour = int(datetime.datetime.now().hour)
    if hour >= 17:
        speak("Okay Sir, Goodnight", head_lable, textarea, bottom_lable)
        speak("Lets talk next day", head_lable, textarea, bottom_lable)
    else:
        speak("Okay Sir", head_lable, textarea, bottom_lable)
        speak("Have a nice day", head_lable, textarea, bottom_lable)
    root.protocol("WM_DELETE_WINDOW", root.withdraw())
    notification.notify(
        title="Srishti",
        message="To wake up me you need to call my name",
        app_icon="srishti.ico",
        timeout=5
    )
    time.sleep(2)
    while True:
        hot = hotword()
        if hot == True:
            break
    # while True:
    #     key = hotword()
    #     if key == "wake up srishti" or key == "weke up drishti":
    #         break
    root.protocol("WM_DELETE_WINDOW", root.deiconify())
    time.sleep(1)
    speak("Welcome back sir", head_lable, textarea, bottom_lable)
    speak("how may I help you", head_lable, textarea, bottom_lable)



def Time(head_lable, textarea, bottom_lable):
    time = datetime.datetime.now().strftime('%H:%M')
    speak(f"The Current time is {time}", head_lable, textarea, bottom_lable)

def Date(head_lable, textarea, bottom_lable):
    date = datetime.date.today()
    day = date.strftime("%A")
    speak(f"The Current date is {date}", head_lable, textarea, bottom_lable)
    speak(f"Today is {day}", head_lable, textarea, bottom_lable)

def WhoAmI(head_lable, textarea, bottom_lable):
    try:
        name = login()
        speak(f"I think you are {name}", head_lable, textarea, bottom_lable)
    except Exception as e:
        print(e)


def location(head_lable, textarea, bottom_lable):
    r = requests.get("https://get.geojs.io/")
    ip_request = requests.get("https://get.geojs.io/v1/ip.json")
    ipAdd = ip_request.json()['ip']

    url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    speak(f"I think we are in {geo_data['country']}'s city {geo_data['city']}, {geo_data['region']} region the timezone {geo_data['timezone']}", head_lable, textarea, bottom_lable)
    speak(f"latitude :{geo_data['latitude']}", head_lable, textarea, bottom_lable)
    speak(f"longitude :{geo_data['longitude']}", head_lable, textarea, bottom_lable)
    speak("anythink else, you want to know?", head_lable, textarea, bottom_lable)

def weather(head_lable, textarea, bottom_lable):
    r = requests.get("https://get.geojs.io/")
    ip_request = requests.get("https://get.geojs.io/v1/ip.json")
    ipAdd = ip_request.json()['ip']
    url = "https://get.geojs.io/v1/ip/geo/" + ipAdd + ".json"
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    city = geo_data['city']
    key = "8b9272a4f84f4c63906130146232105"
    BASE_URL = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}&aqi=yes"
    w_url = BASE_URL
    w_request = requests.get(w_url)
    w_data = w_request.json()
    speak(f"The current weather in Fahrenheit {w_data['current']['temp_f']} and Celsius is {w_data['current']['temp_c']}", head_lable, textarea, bottom_lable)
    speak(f"humidity is {w_data['current']['humidity']}, wind speed is {w_data['current']['wind_kph']}kilometer per Hours", head_lable, textarea, bottom_lable)
    speak(f"pressure {w_data['current']['pressure_mb']}", head_lable, textarea, bottom_lable)
    speak("Anythink else sir", head_lable, textarea, bottom_lable)

def news_report(head_lable, textarea, bottom_lable):
    news_data = news()
    speak("Today's top five news are", head_lable, textarea, bottom_lable)
    for key, value in list(news_data.items())[:5]:
        speak(f"{key}. {value['title'][0]}", head_lable, textarea, bottom_lable)



def newUser(head_lable, textarea, bottom_lable):
    speak("To login new user you need to log out then log in or create a new user", head_lable, textarea, bottom_lable)

##############Input Function##############
def Wikipedia(query, head_lable, textarea, bottom_lable):
    try:
        query = str(query).replace("who is", "").replace("about", "").replace("tell me about", "").replace("what is", "").replace("wikipedia", "")
        len_query = len(query.replace(" ", ""))
        if len_query > 0:
            result = wikipedia.summary(query)
        else:
            speak("Tell me your query in wikipedia", head_lable, textarea, bottom_lable)
            question = takeCommand()
            result = wikipedia.summary(question)
        speak(result, head_lable, textarea, bottom_lable)

    except Exception as e:
        speak('Wikipedia occurs an error', head_lable, textarea, bottom_lable)


def google(query, head_lable, textarea, bottom_lable):
    query = str(query).replace("google", "").replace("search", "").replace("about", "")
    len_query = len(query.replace(" ", ""))
    if len_query > 0:
        pywhatkit.search(query)
        speak("Here is search result", head_lable, textarea, bottom_lable)
    else:
        speak("what should I search?", head_lable, textarea, bottom_lable)
        question = takeCommand(head_lable, textarea, bottom_lable)
        speak("Here is search result", head_lable, textarea, bottom_lable)
        pywhatkit.search(question)

def youtube(query, head_lable, textarea, bottom_lable):
    ans = str(query)
    query = str(query).replace("youtube", "").replace("play video", "").replace("video about", "").replace("latest video", "").replace("music", "").replace("videos", "").replace("play songs", "")
    len_query = len(query.replace(" ", ""))
    if len_query > 0:
        if 'videos' in ans:
            result = f"https://www.youtube.com/results?search_query={query}"
            speak("Here is search result", head_lable, textarea, bottom_lable)
            web.open(result)
        else:
            speak("Here is search result", head_lable, textarea, bottom_lable)
            pywhatkit.playonyt(query)
    else:
        speak("Tell me the video name do you want to search", head_lable, textarea, bottom_lable)
        quest = takeCommand(head_lable, textarea, bottom_lable)
        speak("Here is search result", head_lable, textarea, bottom_lable)
        quest = str(quest)
        if 'random' in quest:
            quest = quest.replace("random", "").replace("play", "").replace("video", "")
            pywhatkit.playonyt(quest)
        elif "videos" in ans:
            quest = quest.replace("videos", "")
            result = f"https://www.youtube.com/results?search_query={quest}"
            web.open(result)
        elif "play songs" in ans:
            quest = quest.replace("play songs", "")
            pywhatkit.playonyt(quest)
        else:
            pywhatkit.playonyt(quest)

def open_ai(query, head_lable, textarea, bottom_lable):
    API_KEY = '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'
    prompt = query
    os.environ['OPENAI_Key'] = API_KEY
    openai.api_key = os.environ['OPENAI_Key']
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=50, temperature=0.7)
    ans = (response['choices'][0]['text'])
    speak(ans, head_lable, textarea, bottom_lable)

def write_program(query, head_lable, textarea, bottom_lable):
    API_KEY = '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'
    query = query.replace('write a program', '').replace('write a code', '').replace('program', '').replace('write a', '')
    print(query)
    print(len(query))
    if len(query) == 0:
        speak("What programme should I write and what type of program should i write?", head_lable, textarea, bottom_lable)
        query = takeCommand(head_lable, textarea, bottom_lable)
        query = str(query)
    else:
        query = str(query)
    prompt = query
    os.environ['OPENAI_Key'] = API_KEY
    openai.api_key = os.environ['OPENAI_Key']
    response = openai.Completion.create(engine='text-davinci-003', prompt=prompt, max_tokens=50, temperature=0.7)
    ans = (response['choices'][0]['text'])
    # speak(ans, head_lable, textarea, bottom_lable)
    speak('tell me the program name that you want to save....', head_lable, textarea, bottom_lable)
    name = takeCommand(head_lable, textarea, bottom_lable)
    if 'python' in query:
        exten = 'py'
    elif 'java' in query:
        if 'public class' in ans:
            ans = ans.replace('public class', 'class')
        exten = 'java'
    elif 'c' in query:
        exten = 'c'
    else:
        exten = 'txt'
    file = open(f'C:\\Users\\arnab\\OneDrive\\Documents\\SRISHTI MAKE CODE\\{name}.{exten}', 'w')
    file.write(ans)
    speak(f'The path where the program save -> C:\\Users\\arnab\\OneDrive\\Documents\\SRISHTI MAKE CODE\\{name}.{exten}', head_lable, textarea, bottom_lable)


def NonInputExecution(query, head_lable, textarea, bottom_lable):

    query = str(query)

    if "time" in query:
        Time(head_lable, textarea, bottom_lable)
    elif "date" in query:
        Date(head_lable, textarea, bottom_lable)
    elif "face" in query:
        WhoAmI(head_lable, textarea, bottom_lable)
    elif "register" in query:
        newUser(head_lable, textarea, bottom_lable)
    elif "location" in query:
        location(head_lable, textarea, bottom_lable)
    elif "weather" in query:
        weather(head_lable, textarea, bottom_lable)
    elif "news" in query:
        news_report(head_lable, textarea, bottom_lable)



def InputExecution(tag, query, head_lable, textarea, bottom_lable):
    query = str(query)

    if 'wikipedia' in tag:
        Wikipedia(query, head_lable, textarea, bottom_lable)

    elif 'search' in tag:
        google(query, head_lable, textarea, bottom_lable)

    elif 'youtube' in tag:
        youtube(query, head_lable, textarea, bottom_lable)

    elif 'chat' in tag:
        open_ai(query, head_lable, textarea, bottom_lable)

    elif 'code' in tag:
        write_program(query, head_lable, textarea, bottom_lable)

