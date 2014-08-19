import graphics
import gameplay

class Explosion:
    pre = 64
    pos = 12

    pos += pre

class Bomb(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "bomb.png", pos)

        self.weapon = Explosion()

        self.box = 16

        self.xVel, self.yVel = (0, 0)
        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.timer += 1
        self.animation.animate(self.sprite)

        self.animation.set(index=lambda: (self.animation.timer / 8) % 2 if self.animation.timer < self.weapon.pre else self.animation.timer - self.weapon.pre)

        self.sprite.draw(display, offset)

    def damage(self):
        return 2

    def living(self):
        return False

    def update(self):
        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.box) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.box) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.box) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.box) % gameplay.tile.size

            self.yVel = 0

        self.applyGravity()

        if self.animation.timer > self.weapon.pre:
            for entity in self.world.entities:
                if entity.living() and self.sprite.collidesWith(entity.sprite):
                    entity.getHurt(self)

        if self.animation.timer > self.weapon.pos:
            self.dead = True

    def collided(self):
        l = int(self.sprite.x - self.box) / gameplay.tile.size
        r = int(self.sprite.x + self.box - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.box) / gameplay.tile.size
        b = int(self.sprite.y + self.box - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player) \
        and self.animation.timer > self.weapon.pre:
            entity.getHurt(self)

    def getHurt(self, origin):
        pass

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.8
        else:  self.yVel = min(self.yVel + 0.5, gameplay.tile.size)
