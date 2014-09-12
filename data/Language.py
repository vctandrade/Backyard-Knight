import json
import data

folder = "lang/"

def loadLanguage():
    global langPack
    with open(folder + data.config.LANG) as f:
        langPack = json.load(f, encoding="latin")

def translate(key):
    if langPack.has_key(key):
        return langPack[key]
    else: return key
