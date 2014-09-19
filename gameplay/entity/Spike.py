import graphics
import gameplay
import pygame
import data
import math

class Spike(object):

    def __init__(self, world, pos, mode, startTime=0, waitTime=128):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: self.animation.timer % 10

        pos[1] = (pos[1] / 32) * 32

        self.sprite = graphics.Sprite(0, "spike.png", pos)
        self.skull = graphics.Sprite(10, "spike.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.dead = False

        self.mode = mode
        self.dir = 1

        if self.mode == "up":
            self.dir = -1
            self.sprite.y += 90

        if self.mode == "down":
            self.sprite.y -= 58
            self.sprite.yScale = -1

        self.skull.y += 16
        self.origin = self.sprite.y

        self.waitTime = waitTime
        self.animation.timer = startTime

    def draw(self, display, offset=(0, 0)):
        self.skull.draw(display, offset)

        self.animation.animate(self.sprite)

        buff = pygame.Surface([78, 180])
        buff.set_colorkey(0xFF00FF)
        buff.fill(0xFF00FF)

        xRect = self.sprite.x - 37
        yRect = round(self.sprite.y - 90)

        self.sprite.draw(buff, [xRect, yRect])

        xRect -= math.floor(offset[0])
        yRect -= math.ceil(offset[1])

        if self.mode == "up":
            pos = (xRect, yRect)
            rect = ((0, 0), (74, self.origin - round(self.sprite.y)))

        if self.mode == "down":
            pos = (xRect, self.origin + 90 - offset[1])
            rect = ((0, 180 - self.sprite.y + self.origin), (74, 180))

        display.blit(buff, pos, rect)

    def update(self):
        self.animation.timer += 1

        self.sprite.y += self.yVel

        if self.collided():

            if cmp(self.yVel, 0) == self.dir:
                if self.dir >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
                else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.moveDown()

            xDis = self.sprite.x - self.world.player.sprite.x
            yDis = self.sprite.y - self.world.player.sprite.y

            distance = ((xDis) ** 2 + (yDis) ** 2) ** 0.5
            distance = max(1, distance)

            self.world.camera.setShake(64000 / distance, 0.8)

            distance = (self.sprite.x - self.world.player.sprite.x) ** 2 + (self.sprite.y - self.world.player.sprite.y) ** 2
            volume = 1000.0 * data.config.SOUND / distance
            if volume > 0.1: data.playSound("spike1.ogg", volume=volume)

        if self.dir * (self.sprite.y - self.origin) >= 180:
            self.moveDown()

        if self.dir * (self.sprite.y - self.origin) <= 0:
            self.yVel = 0
            self.sprite.y = self.origin
            if self.animation.timer >= self.waitTime:
                self.animation.timer = -self.waitTime
                self.moveUp()

                distance = (self.sprite.x - self.world.player.sprite.x) ** 2 + (self.sprite.y - self.world.player.sprite.y) ** 2
                volume = 1000.0 * data.config.SOUND / distance
                if volume > 0.1: data.playSound("spike2.ogg", volume=volume)

    def moveUp(self):
        self.yVel = 9 * self.dir

    def moveDown(self):
        self.yVel = -1.5 * self.dir

    def getHurt(self, origin):
        pass

    def collided(self):
        if cmp(self.sprite.y, self.origin) != self.dir:
            return False

        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        y = int(self.sprite.y + (self.sprite.yCenter + 1) * self.dir) / gameplay.tile.size

        for x in range(l, r + 1):
            if self.world.map[y][x].isColidable():
                return True

        return False

    def damage(self):
        return 1

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if entity.invincibility <= 0:
                if self.mode == "up" and (entity.sprite.y + entity.lowerBox) <= self.origin - 90 \
                or self.mode == "down" and (entity.sprite.y - entity.upperBox) >= self.origin + 90:
                    if self.sprite.collidesWith(entity.sprite):
                        entity.getHurt(self)
