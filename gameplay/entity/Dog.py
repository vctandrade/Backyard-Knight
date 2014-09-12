import graphics
import gameplay

class Dog(object):

    def __init__(self, world, pos):

        self.world = world
        self.world.backyardTimer = 0
        self.world.map = self.world.backyardMap

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: 3 if not self.onSurface() else 2 + (self.animation.timer / 8) % 3 if abs(self.xVel) > 1 else (self.animation.timer / 16) % 2

        self.sprite = graphics.Sprite(0, "dog.png", pos)
        self.xVel, self.yVel = 4 * cmp(self.world.player.sprite.x, self.sprite.x), -4

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        side = cmp(self.world.player.sprite.x, self.sprite.x)

        if side > 0: self.sprite.xScale = 1
        if side < 0: self.sprite.xScale = -1

        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter - 32) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter + 32) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.yVel = 0

        if abs(self.sprite.x - self.world.player.sprite.x) > 100:
            if not self.stuck() and self.onSurface(): self.follow()

        self.applyGravity()

    def follow(self):
        self.xVel = (2.5 - 0.6 * (abs(self.world.player.xVel) == 1.5)) * self.sprite.xScale

    def getHurt(self, origin):
        pass

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def stuck(self):
        side = cmp(self.world.player.sprite.x, self.sprite.x)

        self.sprite.x += side
        stuck = self.collided()
        self.sprite.x -= side

        return stuck

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter - 32) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter + 31) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, origin):
        pass

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.9
        else:  self.yVel = min(self.yVel + 0.5, gameplay.tile.size - 1)

