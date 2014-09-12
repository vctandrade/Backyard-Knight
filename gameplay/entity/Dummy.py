import graphics
import gameplay
import random
import data

class Dummy(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: 32 if self.invincibility <= 0 else 32
        self.sprite = graphics.Sprite(32, "beholder.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.invincibility = 0
        self.dead = False

    def draw(self, display, offset=(0, 0)):
        origin = self.sprite.x

        self.animation.animate(self.sprite)

        if self.animation.timer < 0:
            random.seed(self.animation.timer)
            self.sprite.x += random.random() * 8 - 4

        self.sprite.draw(display, offset)
        self.sprite.x = origin

    def getHurt(self, origin):
        if self.invincibility > 0:
            return

        self.invincibility = origin.weapon.pos - origin.weapon.pre
        self.animation.timer = -8

        data.playSound("wood" + str(random.randint(1, 2)) + ".ogg")

    def damage(self):
        return 0

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.yVel = 0

        self.applyGravity()
        self.invincibility -= 1

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

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if not self.onSurface(): self.yVel = min(self.yVel + 0.5, gameplay.tile.size - 1)
