import time
import librosa
import numpy as np
import sounddevice as sd
import psycopg2
from io import BytesIO
from keras.models import model_from_json
from plyer import notification

def load_model_from_database():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect('postgres://srishti_database_ai_user:JaYaL1A92lAp0ikj0RxGjgKihQ3etVWj@dpg-cic47a95rnuk9qb0sbc0-a.oregon-postgres.render.com/srishti_database_ai')

    # Create a cursor
    cur = conn.cursor()

    # Retrieve the model data from the database
    cur.execute("SELECT model_data FROM model_table ORDER BY id DESC LIMIT 1")
    model_data = cur.fetchone()[0]

    # Load the model from bytes
    model = model_from_json(model_data.tobytes().decode('utf-8'))

    # Commit the changes and close the connection
    cur.close()
    conn.close()

    return model

def hotword():
    # Constants
    fs = 44100
    seconds = 3
    class_names = ["Wake Word NOT Detected", "Wake Word Detected"]

    # Loading the model from the database
    model = load_model_from_database()

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

            if prediction[:, 1] > 0.5:
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
