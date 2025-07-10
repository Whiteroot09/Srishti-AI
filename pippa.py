import sys
import torch
import random
import requests
from Brain import NeuralNet
from test import takeCommand, speak, online, wish_us
from NeuralNetwork import bag_of_word, tokenize
from task import NonInputExecution, InputExecution, exit_open

exit_thread = False

def ai_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    url = 'https://webpage-srishti.onrender.com/data'
    response = requests.get(url)
    intents = response.json()

    FILE = 'saved_model/TrainData.pth'
    data = torch.load(FILE)

    input_size = data['input_size']
    hidden_size = data['hidden_size']
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    return model, intents, all_words, tags, device

def load_model(text, model, intents, all_words, tags, device, root, head_lable, textarea, bottom_lable, name):
    query = str(text)
    if text is not None:
        text = tokenize(text)
        X = bag_of_word(text, all_words)
        X = X.reshape(1, X.shape[0])
        X = torch.from_numpy(X).to(device)

        output = model(X)

        _, predicted = torch.max(output, dim=1)

        tag = tags[predicted.item()]

        probs = torch.softmax(output, dim=1)
        prob = probs[0][predicted.item()]
        if prob.item() > 0.9:
            for intent in intents:
                if tag == intent['tag']:
                    print(tag)
                    reply = random.choice(intent['responses'])
                    print(reply)
                    if reply is not None:
                        if "none" in reply:
                            speak("Sorry I don't understand what you're saying.", head_lable, textarea, bottom_lable)
                            speak("say that again please", head_lable, textarea, bottom_lable)
                        elif "time" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "date" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "face" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "register" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "location" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "weather" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "exit" in reply:
                            exit_open(root, head_lable, textarea, bottom_lable)
                        elif "wikipedia" in reply:
                            InputExecution(reply, query, head_lable, textarea, bottom_lable)
                        elif "search" in reply:
                            InputExecution(reply, query, head_lable, textarea, bottom_lable)
                        elif "yes" in tag:
                            speak(reply, head_lable, textarea, bottom_lable)
                        elif "no" in tag:
                            speak(reply, head_lable, textarea, bottom_lable)
                        elif "youtube" in reply:
                            InputExecution(reply, query, head_lable, textarea, bottom_lable)
                        elif "chat" in reply:
                            InputExecution(reply, query, head_lable, textarea, bottom_lable)
                        elif "code" in reply:
                            InputExecution(reply, query, head_lable, textarea, bottom_lable)
                        elif "news" in reply:
                            NonInputExecution(reply, head_lable, textarea, bottom_lable)
                        elif "log out" in reply:
                            speak(f"Okey {name}, log out", head_lable, textarea, bottom_lable)
                            speak("SRIshti offline", head_lable, textarea, bottom_lable)
                            speak("Just close it it automatic logout", head_lable, textarea, bottom_lable)
                            root.destroy()
                            sys.exit()
                        else:
                            speak(reply, head_lable, textarea, bottom_lable)

                        
def command(root, head_lable, textarea, bottom_lable, name, gender):
    model, intents, all_words, tags, device = ai_model()
    online("srishti online")
    wish_us(gender, head_lable, textarea, bottom_lable)
    while True:
        text = takeCommand(head_lable, textarea, bottom_lable)
        load_model(text, model, intents, all_words, tags, device, root, head_lable, textarea, bottom_lable, name)

