import graphics
import gameplay
import pygame

class Spike(object):

    def __init__(self, world, pos, mode):
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

    def draw(self, display, offset=(0, 0)):
        self.skull.draw(display, offset)

        self.animation.animate(self.sprite)

        buff = pygame.Surface([78, 180])
        buff.set_colorkey(0xFF00FF)
        buff.fill(0xFF00FF)

        xRect = self.sprite.x - 37
        yRect = self.sprite.y - 90

        self.sprite.draw(buff, [xRect, yRect])

        xRect -= offset[0]
        yRect -= offset[1]

        if self.mode == "up":
            pos = (xRect, yRect)
            rect = ((0, 0), (74, self.origin - self.sprite.y))

        if self.mode == "down":
            pos = (xRect, self.origin + 90 - offset[1])
            rect = ((0, 180 - self.sprite.y + self.origin), (74, 180))

        display.blit(buff, pos, rect)

    def update(self):
        self.animation.timer += 1

        self.sprite.y += self.yVel
        self.sprite.x += self.xVel

        if self.collided():
            self.moveDown()

            xDis = self.sprite.x - self.world.player.sprite.x
            yDis = self.sprite.y - self.world.player.sprite.y

            distance = ((xDis) ** 2 + (yDis) ** 2) ** 0.5
            distance = max(1, distance)

            self.world.camera.setShake(64000 / distance, 0.8)

        if abs(self.sprite.y - self.origin) >= 180:
            self.moveDown()

        if abs(self.sprite.y - self.origin) <= 0:
            self.yVel = 0
            if self.animation.timer == 128:
                self.animation.timer = -128
                self.moveUp()

    def moveUp(self):
        self.yVel = 9 * self.dir

    def moveDown(self):
        self.yVel = -1.5 * self.dir

    def getHurt(self, origin):
        pass

    def collided(self):
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
            if self.mode == "up" and (entity.sprite.y + entity.upperBox) < self.origin \
            or self.mode == "down" and (entity.sprite.y - entity.lowerBox) > self.origin:
                entity.getHurt(self)
