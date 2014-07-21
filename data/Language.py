import json
import data

def loadLanguage():
    global langPack
    with open("../../lang/" + data.config.LANG) as f:
        langPack = json.load(f)

def translate(key):
    return langPack[key]
