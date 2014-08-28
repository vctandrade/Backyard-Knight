import pygame
import data

currentMusic = None

def loadImage(imgPath):
    img = pygame.image.load(imgPath).convert_alpha()

    width = img.get_width() * 2
    height = img.get_height() * 2

    img = pygame.transform.scale(img, (width, height))

    return img

def formatValue(value):
    try: value = int(value)
    except:
        try: value = float(value)
        except: pass

    if value == "true": value = True
    if value == "false": value = False

    return value

def playMusic(song):
    global currentMusic
    currentMusic = song

    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(data.config.MUSIC / 100.0)
    pygame.mixer.music.play(-1)

def stopMusic():
    global currentMusic
    currentMusic = None

    pygame.mixer.music.stop()

def getMusic():
    return currentMusic
