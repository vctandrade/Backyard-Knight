import graphics
import gameplay
import random
import math

class Beholder(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "beholder_change.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.health = 1
        self.state = "idle"
        self.dir = 0

        self.invincibility = 0
        self.dead = False

        self.floatTimer = 0


    def draw(self, display, offset=(0, 0)):

        if self.xVel > 0: self.sprite.xScale = -1
        if self.xVel < 0: self.sprite.xScale = 1

        origin = self.sprite.y

        if self.state == "idle":
            self.animation.index = lambda: 0

        if self.state == "walking":
            self.animation.index = lambda: 1 if self.animation.timer < 144 or self.animation.timer > 240 else 2

        if self.state == "running":
            self.animation.index = lambda: 4 if self.animation.timer < 64 else 5 if self.animation.timer < 80 else 6
        if self.state == "dead":
            self.animation.index = lambda: 8 if  self.animation.timer < 16 else 9 if self.animation.timer < 32 else 10

        self.animation.animate(self.sprite)
        self.animation.timer += 1

        if self.state != "dead":
            self.sprite.y += math.cos(self.floatTimer / 32.0) * 8
        if self.state == "dead":
            self.sprite.y = origin + 2

        self.sprite.draw(display, offset)

        self.sprite.y = origin
        self.floatTimer += 1

    def knockBack(self, origin):
        self.xVel = 4 * cmp(self.sprite.x, origin.sprite.x)



    def getHurt(self, origin):
        if self.invincibility > 0 or self.state == "dead":
            return

        self.health -= origin.damage()

        self.invincibility = origin.weapon.pos - origin.weapon.pre

    def damage(self):
        return 1

    def living(self):
        return True

    def playerClose(self):
        return abs(self.sprite.y - self.world.player.sprite.y) < 80 \
        and abs(self.sprite.x - self.world.player.sprite.x) < 420

    def walk(self):
        self.xVel = 2 * self.dir
        self.state = "walking"

    def run(self):
        self.xVel = 4 * self.dir

    def stuck(self):
        self.sprite.x += self.dir
        stuck = self.collided()
        self.sprite.x -= self.dir

        return stuck

    def update(self):
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

        self.applyGravity()

        self.invincibility -= 1

        if self.health <= 0 and self.state != "dead":
            self.xVel = 0
            if self.invincibility < 0:
                self.state = "dead"
                self.animation.timer = 0

        if self.state == "dead":
            return

        if self.state != "running" and self.animation.timer >= 128:
            if self.animation.timer == 128:
                self.dir = random.choice([-1, 1])
            else: self.walk()

            if self.animation.timer > 256 or self.stuck():
                self.state = "idle"
                self.animation.timer = 0

        if self.playerClose():
            if self.state != "running":
                self.animation.timer = 0
                self.dir = cmp(self.world.player.sprite.x, self.sprite.x)
                if self.dir != 0: self.state = "running"
            if self.animation.timer > 64:
                self.run()
            if self.stuck():
                self.state = "idle"
                self.animation.timer = 0

        elif self.animation.timer >= 64:
            self.state = "idle"
            self.animation.timer = 0

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
            if self.health > 0 and self.invincibility <= 0:
                entity.getHurt(self)

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.8
        else:  self.yVel = min(self.yVel + 0.1, 2)

