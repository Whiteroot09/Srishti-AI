import speech_recognition as sr
import assemblyai as aai
import base64

def takeCommand():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            print('Listening...')
            audio = r.listen(mic, phrase_time_limit=4)
            print("Recognizing...")

            # Convert audio data to PCM format
            pcm_data = audio.get_raw_data(convert_rate=16000, convert_width=2)

            # Encode PCM data as Base64
            encoded_data = base64.b64encode(pcm_data).decode('utf-8')

            # Set up the AssemblyAI API
            aai.settings.api_key = "aec2f040d91e471289ef5907c48c61d6"

            # Create a transcriber object
            transcriber = aai.Transcriber()

            # Submit the audio for transcription
            response = transcriber.transcribe(encoded_data)

            # Retrieve the transcript from the response
            transcript = response['text']

            query = transcript if transcript else ""

            print(f"User Said: {query}")
            query = str(query).lower()

    except sr.RequestError:
        print("Could not request results from speech recognition service; check your internet connection")
        return None
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return None
    return query

while True:
    take = takeCommand()
    print(take)
