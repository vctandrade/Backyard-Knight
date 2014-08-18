import data
import os

class Configuration:

    LANG = "en_us"
    WIDTH = 1280
    HEIGHT = 768
    FULLSCREEN = False
    MUSIC = 100
    SOUND = 100

    def __getitem__(self, key): return Configuration.__dict__[key]
    def __setitem__(self, key, value): Configuration.__dict__[key] = value
    def __getattr__(self, key): return self.__getitem__(key)
    def __setattr__(self, key, value): self.__setitem__(key, value)
    def __contains__(self, key): return key in Configuration.__dict__
    def __iter__(self): return Configuration.__dict__.iterkeys()

config = Configuration()

def loadConfig():
    if os.path.isfile("config.ini"):
        with open("config.ini", 'r') as f:
            for line in f:
                try:
                    key, value = line.split(":")
                    key, value = key.strip(), value.strip()
                    assert key in config
                except: continue
                config[key] = data.formatValue(value)

def saveConfig():
    with open("../../config.ini", 'w') as f:
        for k in config:
            if '__' in k: continue
            f.write(k + ": " + str(config[k]).lower() + "\n")
