import graphics
import gameplay
import math

class Spike(object):

    def __init__(self, world, pos):
        self.world = world

        self.state = "down"
        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "spike_change.png", pos)

        self.upLimit = self.sprite.y + 100
        self.downLimit = self.sprite.y

        self.xVel, self.yVel = (0, 0)

        self.upperBox = 16
        self.dead = False

        self.moveTimer = 0

    def draw(self, display, offset=(0, 0)):
        origin = self.sprite.y

        self.animation.index = lambda: (self.animation.timer / 7) % 7

        self.animation.timer += 1
        self.animation.animate(self.sprite)

        if self.animation.timer < 10:
            self.sprite.y += math.cos(self.moveTimer / 4.0) * 20
        else:
            self.sprite.y += math.cos(self.moveTimer / 32.0) * 20

        self.sprite.draw(display, offset)

        self.sprite.y = origin
        self.moveTimer += 1


    def update(self):
        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.yVel = 0


        if self.sprite.y == self.upLimit:
            self.moveDown()
        if self.sprite.y == self.downLimit:
            self.moveUp()

    def moveUp(self):
        self.yVel = 10
        self.state = "up"
    def moveDown(self):
        self.yVel = -2
        self.state = "down"
    def getHurt(self, origin):
        self.world.player.knockBack(self)

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter + self.upperBox) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def damage(self):
        return 2

    def living(self):
        return True

    def GetHurt(self):
        pass

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
                entity.getHurt(self)
