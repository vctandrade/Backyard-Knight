import pygame

def loadImage(imgPath):
    img = pygame.image.load(imgPath)

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
