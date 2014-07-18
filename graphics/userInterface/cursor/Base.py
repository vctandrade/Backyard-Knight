import graphics
import pygame

sprite = None
info = graphics.AnimationInfo()

def draw(display):
    if sprite == None: return
    sprite.draw(display)

def update():
    if sprite == None: return

    info.timer += 1
    info.animate(sprite)
    sprite.x, sprite.y = pygame.mouse.get_pos()

def setDefault():
    global sprite

    pygame.mouse.set_visible(True)
    sprite = None

def setFairy():
    global sprite

    pygame.mouse.set_visible(False)
    sprite = graphics.Sprite(3, "sprite.png", pygame.mouse.get_pos())
    sprite.xScale, sprite.yScale = 2, 2

    info.clear()
    info.set(index=lambda: 3 + (info.timer % 6) / 3)
