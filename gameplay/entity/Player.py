import graphics
import gameplay

class Player(object):

    def __init__(self, world):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "bob.png", (0, 0))

        self.state = "idle"
        self.stance = "standing"

        self.xVel, self.yVel = (0, 0)

        self.knock = 0
        self.invincibility = 0

        self.sideBox = 22
        self.upperBox = 34
        self.lowerBox = 48

        self.health = 6
        self.maxHealth = 6

    def draw(self, display, offset=(0, 0)):
        if self.xVel > 0: self.sprite.xScale = 1
        if self.xVel < 0: self.sprite.xScale = -1

        self.sprite.alpha = 255 - self.invincibility

        if self.stance == "falling":
            self.animation.set(index=lambda: 2)

        if self.stance == "crouched":
            if self.state == "walking":
                self.animation.set(index=lambda: 3 + (self.animation.timer % 8) / 4)
            else: self.animation.set(index=lambda: 3)

        if self.stance == "standing":
            if self.state == "walking":
                self.animation.set(index=lambda: (self.animation.timer % 8) / 4)
            else: self.animation.set(index=lambda: 0)

        if self.knock > 0:
            if self.knock < 64:
                self.animation.set(index=lambda: 6 if self.knock > 10 else 5)
            else: self.animation.set(index=lambda: 7)

        self.animation.timer += 1
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def moveLeft(self):
        if self.knock > 0: return

        if self.stance == "falling": self.xVel = max(self.xVel - 0.2, -3)
        if self.stance == "crouched": self.xVel = max(self.xVel - 0.5, -1.5)
        if self.stance == "standing": self.xVel = max(self.xVel - 1, -3)

        self.state = "walking" if self.state == "idle" else "idle"

    def moveRight(self):
        if self.knock > 0: return

        if self.stance == "falling": self.xVel = min(self.xVel + 0.2, 3)
        if self.stance == "crouched": self.xVel = min(self.xVel + 0.5, 1.5)
        if self.stance == "standing": self.xVel = min(self.xVel + 1, 3)

        self.state = "walking" if self.state == "idle" else "idle"

    def crouch(self):
        if self.stance == "standing" or self.stance == "crouched":
            self.stance = "crouched"
            self.upperBox = 16

    def stand(self):
        self.upperBox = 34

        if self.collided():
            self.crouch()
            return False

        return True

    def jump(self):
        if self.knock > 0: return

        if self.stance == "crouched":
            if self.stand():
                self.yVel = -10

        if self.stance == "standing":
            self.yVel = -9

    def knockBack(self, origin):
        self.knock = 64

        self.xVel = 4 * cmp(self.sprite.x, origin.sprite.x)
        self.yVel = -4

    def damage(self, origin):
        if self.invincibility > 0:
            return

        self.knockBack(origin)
        self.health -= origin.damage

        if self.health > 0:
            self.invincibility = 128

    def update(self):
        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sideBox) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sideBox) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.lowerBox) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.upperBox) % gameplay.tile.size

            self.yVel = 0

        self.applyGravity()

        self.stand()
        self.state = "idle"

        self.invincibility = max(self.invincibility - 1, self.health <= 0)

        for entity in self.world.entities:
            if self.sprite.collidesWith(entity.sprite):
                entity.collidedWith(self)

    def collided(self):
        l = int(self.sprite.x - self.sideBox) / gameplay.tile.size
        r = int(self.sprite.x + self.sideBox - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.upperBox) / gameplay.tile.size
        b = int(self.sprite.y + self.lowerBox - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface():
            if self.knock == 0:
                if self.state == "idle":
                    self.xVel *= 0.6
                self.stance = "standing"

            else: self.xVel *= 0.9

            self.knock = max(self.knock - 1, 0)
            if self.health <= 0: self.knock = 16

        else:
            if self.knock == 0:
                if self.stance == "crouched" and self.yVel >= 0:
                    self.sprite.y += 23
                self.stance = "falling"

            self.yVel = min(self.yVel + 0.5, gameplay.tile.size)
