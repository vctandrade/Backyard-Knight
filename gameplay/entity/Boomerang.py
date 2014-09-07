import graphics
import gameplay
import random

class Crush:
    pre = 32
    pos = 64

class Boomerang(object):

    def __init__(self, summoner, pos):
        self.world = summoner.world
        self.summoner = summoner

        self.animation = graphics.AnimationInfo()
        self.animation.timer = random.randint(0, 24)
        self.animation.index = lambda: 48 + (self.animation.timer / 2) % 12 if self.turn == 1 else 59 - (self.animation.timer / 2) % 12
        self.animation.alpha = lambda: self.animation.timer * 8 if self.animation.timer < 32 else self.invincibility * 8 if self.invincibility >= 0 else 255

        self.sprite = graphics.Sprite(56, "items.png", pos)

        self.weapon = Crush()
        self.setAim(self.world.player)

        self.dead = False
        self.invincibility = -1

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

        if self.sprite.y - offset[1] < -64:
            self.dead = True

    def getHurt(self, origin):
        if self.invincibility == -1 and type(origin) != gameplay.entity.Boomerang:
            side = cmp(self.summoner.sprite.x, self.world.player.sprite.x)

            if side == self.world.player.sprite.xScale:
                self.setAim(self.summoner)
            else: self.xVel = -6 * side

            self.invincibility = -64

    def damage(self):
        return 1

    def setAim(self, target):
        xDist = target.sprite.x - self.sprite.x
        yDist = target.sprite.y - self.sprite.y

        if yDist == 0:
            self.xVel = 6 * cmp(xDist, 0)
            self.yVel = 0

            return

        P = xDist / yDist

        self.yVel = (36 / (P ** 2.0 + 1)) ** 0.5
        self.xVel = (36 - self.yVel ** 2.0) ** 0.5

        if cmp(self.xVel, 0) != cmp(xDist, 0):
            self.xVel *= -1

        if cmp(self.yVel, 0) != cmp(yDist, 0):
            self.yVel *= -1

        self.turn = cmp(self.xVel, 0)

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

        if self.invincibility < 0:
            for entity in self.world.entities:
                if entity != self and self.sprite.collidesWith(entity.sprite):
                    entity.getHurt(self)

        if self.invincibility > 0: self.invincibility -= 1
        else: self.invincibility = min(self.invincibility + 1, -1)

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        if l < 0 or r >= len(self.world.map[0]):
            return False
        if t < 0 or b >= len(self.world.map):
            return False

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if self.invincibility == -1:
                entity.getHurt(self)
