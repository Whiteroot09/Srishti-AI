from basic_command import speak, takeCommand
from task import Main
from prediction import hotword


if __name__ == '__main__':
    try:
        while True:
            word = hotword()
            if word == True:
                speak('Welcome back sir, How may I help you.')
                Main()
    except Exception as e:
        speak(e)
