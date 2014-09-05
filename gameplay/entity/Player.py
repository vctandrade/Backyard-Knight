import graphics
import gameplay
import data

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
        self.upperBox = 90
        self.lowerBox = 48

        self.health = 6
        self.maxHealth = 6

        self.weapon = gameplay.item.Spear()
        self.item = None

        self.score = 0

        self.flashTimer = 0
        self.flashMode = None
        self.interactibles = set()

    def draw(self, display, offset=(0, 0)):
        if self.xVel > 0: self.sprite.xScale = 1
        if self.xVel < 0: self.sprite.xScale = -1

        if self.xVel > 0: self.weapon.sprite.xScale = 1
        if self.xVel < 0: self.weapon.sprite.xScale = -1

        self.sprite.alpha = 255 - min(self.invincibility, 128)

        if self.stance == "falling":
            if self.state == "attacking":
                self.animation.set(index=lambda: 14 if self.animation.timer < self.weapon.pre else 15)
                self.weapon.sprite.index = 6 if self.animation.timer < self.weapon.pre else 7 if self.animation.timer < self.weapon.swing else 8
            else: self.animation.set(index=lambda: 4)

        if self.stance == "crouched":
            if self.state == "walking":
                self.animation.set(index=lambda: 5 + (self.animation.timer / 8) % 2)
            elif self.state == "attacking":
                self.animation.set(index=lambda: 12 if self.animation.timer < self.weapon.pre else 13)
                self.weapon.sprite.index = 3 if self.animation.timer < self.weapon.pre else 4 if self.animation.timer < self.weapon.swing else 5
            else: self.animation.set(index=lambda: 5)

        if self.stance == "standing":
            if self.state == "walking":
                self.animation.set(index=lambda: (self.animation.timer / 8) % 4)
            elif self.state == "attacking":
                self.animation.set(index=lambda: 10 if self.animation.timer < self.weapon.pre else 11)
                self.weapon.sprite.index = 0 if self.animation.timer < self.weapon.pre else 1 if self.animation.timer < self.weapon.swing else 2
            else: self.animation.set(index=lambda: 0)

        if self.state == "attacking":
            self.weapon.sprite.x = self.sprite.x + self.weapon.xFix[self.weapon.sprite.index] * self.weapon.sprite.xScale
            self.weapon.sprite.y = self.sprite.y + self.weapon.yFix[self.weapon.sprite.index]

        if self.knock > 0:
            if self.knock < 64:
                self.animation.set(index=lambda: 8 if self.knock > 10 else 7)
            else: self.animation.set(index=lambda: 9)

        self.animation.animate(self.sprite)

        if self.state == "attacking":
            if type(self.weapon) == gameplay.item.Spear:
                self.sprite.index += 6

        self.sprite.draw(display, offset)

        if self.state == "attacking":
            self.weapon.sprite.draw(display, offset)

    def moveLeft(self):
        if self.knock > 0 or self.state == "attacking": return

        if self.stance == "falling": self.xVel = max(self.xVel - 0.2, -2.5)
        if self.stance == "crouched": self.xVel = max(self.xVel - 0.5, -1.5)
        if self.stance == "standing": self.xVel = max(self.xVel - 1, -2.5)

        self.state = "walking" if self.state == "idle" else "idle"

    def moveRight(self):
        if self.knock > 0 or self.state == "attacking": return

        if self.stance == "falling": self.xVel = min(self.xVel + 0.2, 2.5)
        if self.stance == "crouched": self.xVel = min(self.xVel + 0.5, 1.5)
        if self.stance == "standing": self.xVel = min(self.xVel + 1, 2.5)

        self.state = "walking" if self.state == "idle" else "idle"

    def crouch(self):
        if self.state == "attacking": return

        if self.stance == "standing" or self.stance == "crouched":
            self.stance = "crouched"
            self.upperBox = 16

    def stand(self):
        if self.state == "attacking": return

        self.upperBox = 38

        if self.collided():
            self.crouch()
            return False

        return True

    def jump(self):
        if self.state == "attacking": return

        if self.knock > 0: return

        if self.stance == "crouched":
            if self.stand():
                self.yVel = -10

        if self.stance == "standing":
            self.yVel = -9

    def useItem(self):
        if self.state == "attacking" or self.knock > 0 \
        or not self.item: return
        self.item.use(self)

    def interact(self):
        if self.state == "attacking" or self.knock > 0:
            return

        for entity in self.interactibles:
            entity.use()

    def attack(self):
        if self.state == "attacking" or self.knock > 0 \
        or not self.weapon: return

        self.state = "attacking"
        self.animation.timer = 0

    def knockBack(self, origin):
        self.knock = 64
        self.state = "idle"

        self.xVel = 4 * cmp(self.sprite.x, origin.sprite.x)
        if self.stand(): self.yVel = -4

        else: self.knock -= 1

    def getHurt(self, origin):
        if self.invincibility > 0:
            return

        self.knockBack(origin)
        self.health -= origin.damage()

        if self.health > 0:
            self.invincibility = 128

        self.animation.timer = 0

    def damage(self):
        return self.weapon.damage

    def update(self):
        self.animation.timer += 1
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

        if self.state == "attacking" and self.animation.timer > self.weapon.pos:
            self.state = "idle"

        self.applyGravity()
        self.stand()

        if self.state != "attacking": self.state = "idle"

        if self.state == "attacking":
            if self.animation.timer == self.weapon.pre and self.onSurface():
                self.xVel = self.weapon.jump * self.sprite.xScale
            if self.weapon.pre < self.animation.timer < self.weapon.swing:
                for entity in self.world.entities:
                    if self.weapon.sprite.collidesWith(entity.sprite):
                        entity.getHurt(self)
            self.weapon.sprite.x = self.sprite.x + self.weapon.xFix[self.weapon.sprite.index] * self.weapon.sprite.xScale
            self.weapon.sprite.y = self.sprite.y

        self.invincibility = max(self.invincibility - 1, self.health <= 0)

        for entity in self.world.entities:
            if self.sprite.collidesWith(entity.sprite):
                entity.collidedWith(self)

    def collided(self):
        l = int(self.sprite.x - self.sideBox) / gameplay.tile.size
        r = int(self.sprite.x + self.sideBox - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.upperBox) / gameplay.tile.size
        b = int(self.sprite.y + self.lowerBox - 1) / gameplay.tile.size

        if l < 0 or r >= len(self.world.map[0]):
            return True

        if b >= len(self.world.map):
            if t == len(self.world.map) + 1:
                self.sprite.y += gameplay.tile.size
                data.playSound("fall.ogg")
                self.animation.timer = 0
                self.health = 0
            self.xVel *= 0.6
            return False

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
                if self.state != "walking":
                    self.xVel *= 0.6
                if self.state != "attacking" or self.stance == "falling":
                    self.stance = "standing"

            else: self.xVel *= 0.9

            self.knock = max(self.knock - 1, 0)
            if self.health <= 0: self.knock = 16

        else:
            if self.state == "attacking" and self.stance != "falling":
                self.xVel = max(-5, min(self.xVel * 0.2, 5))
            if self.knock == 0:
                if self.stance == "crouched" and self.yVel >= 0:
                    self.sprite.y += 23
                self.stance = "falling"

            self.yVel = min(self.yVel + 0.5, gameplay.tile.size - 1)
