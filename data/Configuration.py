import data
import os

class Configuration:
    WIDTH = 1024
    HEIGHT = 768
    LANG = "en_us"
        
    def __getitem__(self, key): return Configuration.__dict__[key]
    def __setitem__(self, key, value): Configuration.__dict__[key] = value
    def __contains__(self, key): return key in Configuration.__dict__
    def __iter__(self):
        for k in Configuration.__dict__: yield k

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

def saveConfig(filePath):
    with open(filePath, 'w') as f:
        for k in config:
            if '__' in k: continue
            f.write(k + ": " + str(config[k]) + "\n")
