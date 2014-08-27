import graphics
import Handler

def load():
    global sprite, info

    sprite = graphics.Sprite(3, "sprite.png", (0, 0))

    info = graphics.AnimationInfo()
    info.set(index=lambda: 3 + (info.timer % 6) / 3)

def setFairy(): Handler.setCursor(sprite, info)
