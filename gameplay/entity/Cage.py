import graphics
import gameplay
import random
import math
import data

class Cage (object):

    def __init__(self, world, pos):

        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: 0 if self.health > 0 else (self.animation.timer / 16.0) % 4 if self.animation.timer < 64 else 5
        self.animation.alpha = lambda: 255 if self.health > 0 or self.animation.timer < 64 else 384 - self.world.backyardTimer

        self.sprite = graphics.Sprite(0, "cage.png", pos)

        self.xVel, self.yVel = (0, 1.5)

        self.health = 4
        self.dead = False

        self.invincibility = 0
        self.floatTimer = 0

    def draw(self, display, offset=(0, 0)):

        xOrigin = self.sprite.x
        yOrigin = self.sprite.y

        self.animation.animate(self.sprite)

        if self.animation.timer < 0:
            random.seed(self.animation.timer)
            self.sprite.x += random.random() * 4 - 2
            self.sprite.y += random.random() * 4 - 2

        self.sprite.draw(display, offset)

        self.sprite.x = xOrigin
        self.sprite.y = yOrigin

    def update(self):
        self.animation.timer += 1
        self.floatTimer += 1

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

        if not self.onSurface():
            self.sprite.x += math.cos(self.floatTimer / 16.0)
        else: self.sprite.x = int(self.sprite.x)

        self.invincibility -= 1

        if self.health <= 0 and self.animation.timer == 64:
            self.world.entities.append(gameplay.entity.Dog(self.world, (self.sprite.x, self.sprite.y - 20)))

        if self.sprite.alpha <= 0:
            self.world.entities.append(gameplay.entity.Neighbour())
            self.dead = True

    def damage(self):
        return 0

    def getHurt(self, origin):
        if self.invincibility > 0 or self.health <= 0:
            return

        self.health -= origin.damage()
        self.invincibility = origin.weapon.pos - origin.weapon.pre

        self.animation.timer = -8

        data.playSound("metal" + str(random.randint(1, 2)) + ".ogg")

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
