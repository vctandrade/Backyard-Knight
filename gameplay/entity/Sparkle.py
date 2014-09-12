import graphics
import gameplay
import random

class Sparkle(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.alpha = lambda: 255 - self.animation.timer * 4
        self.sprite = graphics.Sprite(16, "orb.png", pos)

        self.xVel, self.yVel = 0, -1

        self.sprite.x += random.random() * 48 - 32
        self.sprite.y += random.random() * 64 - 32

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def getHurt(self, origin):
        pass

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.dead = True
            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.dead = True
            self.yVel = 0

        if self.animation.timer >= 64:
            self.dead = True

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        pass
