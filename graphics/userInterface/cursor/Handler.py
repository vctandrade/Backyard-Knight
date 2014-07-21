import pygame
import graphics

sprite = None
info = graphics.AnimationInfo()

def init():
    graphics.userInterface.cursor.Fairy.load()

def draw(display):
    if sprite == None: return
    sprite.draw(display)

def update():
    if sprite == None: return

    info.timer += 1
    info.animate(sprite)
    sprite.x, sprite.y = pygame.mouse.get_pos()

def setCursor(newSprite, newInfo=None):
    global sprite, info

    if newInfo == None: info = graphics.AnimationInfo()
    elif info != newInfo: info = newInfo

    if (sprite == None) != (newSprite == None):
        if newSprite == None: pygame.mouse.set_visible(True)
        else: pygame.mouse.set_visible(False)

    sprite = newSprite

def setDefault(): setCursor(None)
