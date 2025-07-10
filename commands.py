from test import takeCommand
from pippa import ai_model, load_model
def command(root, head_lable, textarea, bottom_lable, name):
    model, intents, all_words, tags, device = ai_model()
    while True:
        text = takeCommand(head_lable, textarea, bottom_lable)
        load_model(text, model, intents, all_words, tags, device, root, head_lable, textarea, bottom_lable, name)