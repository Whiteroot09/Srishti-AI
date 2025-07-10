import threading
import time
import sounddevice as sd
import numpy as np
from tensorflow import keras
from keras.models import load_model
import pyttsx3

# SETTING UP TEXT TO SPEECH
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.endLoop()


# CONSTANTS
fs = 44100
seconds = 3

model = load_model("saved_model/WWD.h5")


# LISTENING FUNCTION
def listener():
    while True:
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        mfcc_processed = extract_features(myrecording)
        prediction(mfcc_processed)
        time.sleep(0.001)


# FEATURE EXTRACTION FUNCTION
def extract_features(audio):
    # Normalize audio
    audio = audio / np.max(np.abs(audio))

    # Extract MFCC features
    mfcc = np.mean(np.abs(np.fft.fft(audio)[:40]), axis=1)

    return mfcc


# TARGET WORD DETECTION FUNCTION
def is_word_detected(y):
    # Implement your logic to detect the target word
    # You can use a keyword spotting technique or a specific word recognition model

    # Example: Detecting the word "hello"
    threshold = 0.1  # Adjust the threshold as needed
    word_index = 0  # Assuming the target word index is 0 in the predictions

    word_probability = model.predict(np.expand_dims(y, axis=0))[:, word_index]
    if word_probability > threshold:
        return True
    else:
        return False


# PREDICTION FUNCTION
def prediction(y):
    prediction = model.predict(np.expand_dims(y, axis=0))
    if prediction[:, 1] > 0.96:
        if engine._inLoop:
            engine.endLoop()
        if is_word_detected(y):
            speak("Target word detected!")
        else:
            speak("Word not detected.")
    time.sleep(0.1)


# MAIN THREAD
if __name__ == '__main__':
    listen_thread = threading.Thread(target=listener, name="ListeningFunction")
    listen_thread.start()
