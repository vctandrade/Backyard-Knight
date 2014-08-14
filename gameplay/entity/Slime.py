import graphics
import gameplay
import random

class Slime(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.timer = random.randint(0, 24)
        self.sprite = graphics.Sprite(0, "slime.png", pos)

        self.topBox = 16

        self.xVel, self.yVel = (0, 0)

        self.jumpTimer = random.randint(96, 128)
        self.health = 1

        self.invincibility = 0
        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.timer += 1
        self.animation.animate(self.sprite)

        self.sprite.draw(display, offset)

    def moveLeft(self):
        if self.onSurface():
            self.xVel = -5 - random.random()
            self.yVel = -6

    def moveRight(self):
        if self.onSurface():
            self.xVel = 5 + random.random()
            self.yVel = -6

    def knockBack(self, origin):
        self.xVel = 4 * cmp(self.sprite.x, origin.sprite.x)
        self.yVel = -4

    def getHurt(self, origin):
        if self.invincibility > 0:
            return

        self.knockBack(origin)
        self.health -= origin.damage()

        self.invincibility = origin.weapon.swing - origin.weapon.pre

    def damage(self):
        return 1

    def update(self):
        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter + self.topBox) % gameplay.tile.size

            self.yVel = 0

        self.applyGravity()

        self.invincibility -= 1

        if self.health <= 0:
            if self.invincibility < -20:
                self.dead = True
            return

        if self.jumpTimer == 0:
            if random.random() < 0.5:
                self.moveLeft()
            else: self.moveRight()
            self.jumpTimer = random.randint(96, 128)
        self.jumpTimer -= 1

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter + self.topBox) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if self.health > 0:
                entity.getHurt(self)

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.8
        else:  self.yVel = min(self.yVel + 0.5, gameplay.tile.size)
