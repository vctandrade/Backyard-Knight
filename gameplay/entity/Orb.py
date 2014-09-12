import graphics
import gameplay
import random
import data

class Orb(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: (self.animation.timer / 4) % 15
        self.sprite = graphics.Sprite(0, "orb.png", pos)

        self.xVel = random.random() * 1 - 0.5
        self.yVel = -random.random() * 1 - 1

        self.sprite.x += random.random() * 32 - 16
        self.sprite.y += random.random() * 32 - 16

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        if self.animation.timer < 768 \
        or int(16.0 * self.animation.timer / (1280 - self.animation.timer)) % 4:
            self.animation.animate(self.sprite)
            self.sprite.draw(display, offset)

    def getHurt(self, origin):
        pass

    def playerClose(self):
        xDist = self.world.player.sprite.x - self.sprite.x
        yDist = self.world.player.sprite.y - self.sprite.y

        return xDist ** 2 + yDist ** 2 < 128 ** 2

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.xVel *= -1

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.yVel *= -0.8
            if abs(self.yVel) < 2: self.yVel = cmp(self.yVel, 0) * 2

        if self.playerClose():
            xDist = self.world.player.sprite.x - self.sprite.x
            yDist = self.world.player.sprite.y - self.sprite.y

            P = xDist / yDist

            xAcel = (36 / (P ** 2.0 + 1)) ** 0.5
            yAcel = (36 - xAcel ** 2.0) ** 0.5

            dist = (xDist ** 2 + yDist ** 2) ** 0.5
            if abs(dist) < 1: dist = cmp(dist, 0)

            self.xVel += xAcel / dist * cmp(xDist, 0)
            self.yVel += yAcel / dist * cmp(yDist, 0)

        self.applyGravity()

        if self.animation.timer >= 1024:
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
        if not self.dead and not entity.dead:
            if isinstance(entity, gameplay.entity.Player):
                if self.sprite.collidesWith(entity.sprite):
                    data.playSound("orb.ogg")
                    entity.score += 5
                    self.dead = True

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.6
        else:  self.yVel = min(self.yVel + 0.2, gameplay.tile.size - 1)
