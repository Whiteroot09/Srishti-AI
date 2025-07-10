import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

    try:
        # Use the recognizer to convert speech to text
        text = r.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from the speech recognition service:", str(e))