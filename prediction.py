import time
import librosa
import numpy as np
import sounddevice as sd
from keras.models import load_model
from plyer import notification


def hotword():
    # Constants
    fs = 44100
    seconds = 3
    class_names = ["Wake Word NOT Detected", "Wake Word Detected"]

    # Loading the saved model
    model = load_model("saved_model/WWD.pkl")

    print("Prediction Started:")

    stream = sd.InputStream(channels=1, samplerate=fs)

    with stream:
        audio, status = stream.read(int(seconds * fs))
        if status:
            print("Error:", status)
        else:
            audio = audio.flatten()

            n_fft = len(audio) // 2
            n_mels = 40
            fmax = 8000
            mfcc = librosa.feature.mfcc(y=audio, sr=fs, n_mfcc=40, n_fft=n_fft, hop_length=n_fft // 2,
                                        n_mels=n_mels, fmax=fmax)
            mfcc_processed = np.mean(mfcc.T, axis=0)
            prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))

            if prediction[:, 1] > 0.9:
                print("Wake Word Detected")
                print("Confidence:", prediction[:, 1])
                notification.notify(
                    title="Wake Word Detected",
                    message="Wake word has been detected!",
                    app_icon="srishti.ico",
                    timeout=5
                )
                time.sleep(2)
                return True
            else:
                print("Wake Word NOT Detected")
                print("Confidence:", prediction[:, 0])
                time.sleep(2)
                return False
# while True:
#     print(hotword())