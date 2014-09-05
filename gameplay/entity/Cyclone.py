import graphics
import gameplay

class Cyclone(object):

    def __init__(self, world, pos, direction):
        self.world = world

        self.maxTime = 148

        self.animation = graphics.AnimationInfo()
        self.animation.index = lambda: 56 + (self.animation.timer / 4) % 4
        self.animation.alpha = lambda: self.animation.timer * 16 if self.animation.timer < 16 else 255 if self.animation.timer < self.maxTime else 255 - (self.animation.timer - self.maxTime) * 4

        self.sprite = graphics.Sprite(56, "bob.png", pos)

        self.xVel = 4 * direction
        self.yVel = 0

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def getHurt(self, origin):
        pass

    def damage(self):
        return 1

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

            self.yVel = 0

        if self.animation.timer >= self.maxTime + 64:
            self.dead = True

        self.applyGravity()

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
            entity.getHurt(self)

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if not self.onSurface(): self.yVel = min(self.yVel + 0.5, 6)
