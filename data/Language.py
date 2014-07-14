import json

def loadLanguage(lang):
    global langPack
    with open("../../lang/" + lang) as f:
        langPack = json.load(f)

def translate(key):
    return langPack[key]