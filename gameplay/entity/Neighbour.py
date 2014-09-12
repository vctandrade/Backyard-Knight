import graphics
import gameplay
import random
import data

class Neighbour (object):

    def __init__(self):

        self.animation = graphics.AnimationInfo()
        self.animation.alpha = lambda: self.animation.timer * 2

        self.sprite = graphics.Sprite(3, "neighbour.png", (816 + data.config.WIDTH * 0.4, 380))

        self.dead = False

    def draw(self, display, offset=(0, 0)):

        xOrigin = self.sprite.x

        self.animation.animate(self.sprite)

        if self.animation.timer % 100 < 20 :
            random.seed(self.animation.timer)
            self.sprite.x += random.random() * 2 - 1

        self.sprite.draw(display, offset)

        self.sprite.x = xOrigin

    def update(self):
        self.animation.timer += 1

    def damage(self):
        return 0

    def getHurt(self, origin):
        pass

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        if t < 0: return False

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        pass
