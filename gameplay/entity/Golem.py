import graphics
import gameplay

class Golem(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "golem.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.sprite.xCenter = 48

        self.sprite.xScale = cmp(self.world.player.sprite.x, self.sprite.x)
        if self.sprite.xScale == 0: self.sprite.xScale = -1
        if self.sprite.xScale == -1: self.sprite.x -= 180

        self.lowerBox = 106
        self.upperBox = 54

        self.health = 4

        self.state = "idle"

        self.invincibility = 0
        self.dead = False

    @property
    def leftBox(self):
        if self.state == "attacking" and self.animation.timer < 48:
            return 46 - 52 if self.sprite.xScale == 1 else 66 + 52 - self.sprite.width + 2 * self.sprite.xCenter
        return 46 if self.sprite.xScale == 1 else 66 - self.sprite.width + 2 * self.sprite.xCenter

    @property
    def rightBox(self):
        if self.state == "attacking" and self.animation.timer < 48:
            return 66 - 52 if self.sprite.xScale == 1 else 46 + 52 + self.sprite.width - 2 * self.sprite.xCenter
        return 66 if self.sprite.xScale == 1 else 46 + self.sprite.width - 2 * self.sprite.xCenter

    def draw(self, display, offset=(0, 0)):
        origin = self.sprite.x, self.sprite.y

        if self.state == "attacking":
            self.animation.index = lambda: 8 + (self.animation.timer / 12) % 4 if self.animation.timer < 48 \
            else 16 + (self.animation.timer / 8) % 6

        if self.state == "idle":
            self.animation.index = lambda: (self.animation.timer / 32) % 3

        if self.state == "dead":
            self.animation.index = lambda: 24 + (self.animation.timer / 8) % 5 if self.animation.timer < 40 else 28
            self.sprite.x -= 78 * self.sprite.xScale

        self.animation.animate(self.sprite)
        self.animation.timer += 1

        if self.invincibility > 0: self.sprite.index += 32

        self.sprite.draw(display, offset)
        self.sprite.x, self.sprite.y = origin

    def attack(self):
        self.state = "attacking"
        self.animation.timer = 0
        self.sprite.x -= 52 * self.sprite.xScale

    def knockBack(self, origin):
        pass

    def getHurt(self, origin):
        if self.invincibility > 0 or self.state == "dead":
            return

        self.knockBack(origin)
        self.health -= origin.damage()

        self.invincibility = origin.weapon.pos - origin.weapon.pre

    def damage(self):
        return 3 if self.state == "attacking" and 48 <= self.animation.timer < 96 else 1

    def living(self):
        return True

    def update(self):
        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.rightBox) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.leftBox) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.lowerBox) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.upperBox) % gameplay.tile.size

            self.yVel = 0

        self.applyGravity()

        self.invincibility -= 1

        if self.health <= 0 and self.state != "dead":
            if self.state == "attacking" and self.animation.timer < 48:
                self.sprite.x += 52 * self.sprite.xScale
            self.state = "idle"

            if self.invincibility < 0:
                self.state = "dead"
                self.animation.timer = 0
                self.world.camera.setShake(512, 0.95)

        if self.state == "dead":
            return

        if self.state != "attacking" or self.animation.timer >= 96:
            self.state = "idle"

            if self.world.player.health > 0 and abs(self.world.player.sprite.y - self.sprite.y) < 128:
                k = self.sprite.x
                if self.sprite.xScale == -1:
                    k += self.sprite.width - 2 * self.sprite.xCenter

                if 0 < (self.world.player.sprite.x - k) * self.sprite.xScale < 256:
                    if self.animation.timer >= 256: self.attack()

        if self.state == "attacking" and self.animation.timer == 48:
            self.world.camera.setShake(1024, 0.9)
            self.sprite.x += 52 * self.sprite.xScale

    def collided(self):
        l = int(self.sprite.x - self.leftBox) / gameplay.tile.size
        r = int(self.sprite.x + self.rightBox - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.upperBox) / gameplay.tile.size
        b = int(self.sprite.y + self.lowerBox - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if self.health > 0 and self.invincibility <= 0:
                k = self.sprite.width - 2 * self.sprite.xCenter
                if self.sprite.xScale == -1: self.sprite.x += k
                entity.getHurt(self)
                if self.sprite.xScale == -1: self.sprite.x -= k

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface() and self.state != "walking": self.xVel *= 0.6
        else:  self.yVel = min(self.yVel + 0.5, gameplay.tile.size - 1)
