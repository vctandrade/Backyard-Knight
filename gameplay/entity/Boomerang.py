import graphics
import gameplay
import random

class Boomerang(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.timer = random.randint(0, 24)
        self.sprite = graphics.Sprite(56, "items.png", pos)

        self.setAim(self.world.player)

        self.dead = False
        self.invincibility = -1

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.animation.index = lambda: 48 + (self.animation.timer / 2) % 12

        if self.invincibility >= 0:
            self.animation.alpha = lambda: self.invincibility * 8

        self.sprite.draw(display, offset)

    def getHurt(self, origin):
        if self.invincibility < 0:
            if (self.world.player.sprite.x, self.world.entities[7].sprite.x) == self.world.player.sprite.xScale:
                self.setAim(self.world.entities[7])
            else: self.xVel *= -1

    def damage(self):
        return 1

    def living(self):
        return True

    def setAim(self, target):
        xDist = target.sprite.x - self.sprite.x
        yDist = target.sprite.y - self.sprite.y

        P = xDist / yDist

        self.yVel = (36 / (P ** 2 + 1)) ** 0.5 / 3
        self.xVel = (36 - self.yVel ** 2) ** 0.5 / 3

        if cmp(self.xVel, 0) != cmp(xDist, 0):
            self.xVel *= -1

        if cmp(self.yVel, 0) != cmp(yDist, 0):
            self.yVel *= -1

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.xVel *= -0.5
            self.yVel *= 0.5

            if self.invincibility < 0:
                self.invincibility = 32

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.xVel *= 0.5
            self.yVel *= -0.5

            if self.invincibility < 0:
                self.invincibility = 32

        if self.invincibility == 0:
            self.dead = True

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
        if isinstance(entity, gameplay.entity.Player):
            if self.invincibility <= 0:
                entity.getHurt(self)
