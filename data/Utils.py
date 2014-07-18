import pygame

def loadImage(imgPath):
    img = pygame.image.load(imgPath)
    img.set_colorkey(0xFF00FF)

    return img

def formatValue(value):
    if value == "true": value = True
    if value == "false": value = False

    try: value = int(value)
    except:
        try: value = float(value)
        except: pass

    return value
