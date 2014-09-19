import graphics
import gameplay
import random
import pygame
import data
import math

class Boss(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "boss.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.health = 16
        self.state = "idle"
        self.dir = random.choice([-1, 1])

        self.invincibility = 0
        self.dead = False

        self.floatTimer = 0
        self.boomerangTimer = random.randint(150, 300)
        self.cycloneTimer = random.randint(300, 450)
        self.animation.timer = 64

        self.score = 2500

    def draw(self, display, offset=(0, 0)):
        if self.dir > 0: self.sprite.xScale = 1
        if self.dir < 0: self.sprite.xScale = -1

        xOrigin = self.sprite.x
        yOrigin = self.sprite.y

        if self.state == "idle":
            self.animation.index = lambda: 0
            self.animation.alpha = lambda: 255

        if self.state == "boomerang":
            self.animation.index = lambda: 1 + (self.animation.timer / 8) if self.animation.timer < 24 else 4
            self.animation.alpha = lambda: 255

        if self.state == "cyclone":
            self.animation.index = lambda: 0 if self.animation.timer < 48 else 8 + (self.animation.timer - 48) / 8 if self.animation.timer < 80 else 12 if self.animation.timer < 136 else 0
            self.animation.alpha = lambda: abs(self.animation.timer - 32) * 8 if self.animation.timer < 104 else abs(self.animation.timer - 136) * 8

        if self.state == "hurt":
            self.animation.index = lambda: 17 + (self.animation.timer / 8) % 3 if self.animation.timer > 320 else 16
            self.animation.alpha = lambda: 255

        if self.state == "dying":
            self.animation.index = lambda: 40
            self.animation.alpha = lambda: 512 - self.animation.timer

        self.animation.animate(self.sprite)

        if self.invincibility > 0 and self.state != "dying": self.sprite.index += 24

        if self.state == "dying" or (self.state == "hurt" and 192 <= self.animation.timer < 320):
            random.seed(self.animation.timer)
            self.sprite.x += random.random() * 3 - 1.5
            self.sprite.y += random.random() * 3 - 1.5

        if self.yVel < 0: self.sprite.x += round(math.cos(self.floatTimer / 16.0) * 4)
        if self.state != "dying": self.sprite.y += round(math.sin(self.floatTimer / 16.0) * 4)


        self.sprite.draw(display, offset)

        self.sprite.x = xOrigin
        self.sprite.y = yOrigin

    def move(self):
        self.xVel = 4 * self.dir

    def getHurt(self, origin):
        if self.invincibility > 0 \
        or self.sprite.alpha < 128 \
        or self.health <= 0:
            return

        if type(origin) == gameplay.entity.Boomerang:
            if self.sprite.y < 384:
                self.animation.timer = 0
                self.state = "hurt"
        data.playSound("hit.ogg")

        self.health -= origin.damage()
        self.invincibility = origin.weapon.pos - origin.weapon.pre

    def damage(self):
        return 0

    def update(self):
        self.floatTimer += 1
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter + 32) % gameplay.tile.size
            else: self.sprite.x += gameplay.tile.size - (self.sprite.x - self.sprite.xCenter - 32) % gameplay.tile.size

            self.xVel = 0

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % gameplay.tile.size
            else: self.sprite.y += gameplay.tile.size - (self.sprite.y - self.sprite.yCenter) % gameplay.tile.size

            self.yVel = 0

        if abs(self.xVel) < 0.1: self.xVel = 0
        if abs(self.yVel) < 0.1: self.yVel = 0

        self.invincibility -= 1
        self.boomerangTimer = max(self.boomerangTimer - 1, 0)
        self.cycloneTimer = max(self.cycloneTimer - 1, 0)

        self.applyGravity()

        if self.health <= 0:
            if self.state != "dying":
                self.world.camera.setShake(512, 0.992)
                pygame.mixer.music.fadeout(7400)
                self.world.freezeTimer = 0
                self.animation.timer = 0
                self.state = "dying"

            if self.animation.timer == 512 and not self.world.player.dead:
                data.playMusic("win-intro.ogg", repeat=False)

            if self.animation.timer == 528:
                self.dead = True

                pos = (816, self.world.camera.y - 128)
                self.world.entities.append(gameplay.entity.Cage(self.world, pos))

            if self.score > 0 and not self.world.player.dead:
                if not self.score % 60: data.playSound("orb.ogg")
                self.world.player.score += 10
                self.score -= 10

            return

        if self.state == "idle" and self.world.player.health > 0:

            if self.boomerangTimer == 0 and abs(self.sprite.x - self.world.player.sprite.x) >= 192:
                self.dir = cmp(self.sprite.x, self.world.player.sprite.x)
                self.boomerangTimer = random.randint(150, 300)
                self.state = "boomerang"
                self.animation.timer = 0

            if self.cycloneTimer == 0:
                self.cycloneTimer = random.randint(300, 450)
                self.animation.timer = 0
                self.state = "cyclone"

            if self.animation.timer >= 64:
                self.move()

                if abs(self.sprite.x - 816) > 328 \
                and cmp(self.sprite.x, 816) == self.dir:
                    self.animation.timer = 0
                    self.dir *= -1

        if self.state == "boomerang":
            if self.animation.timer == 24:
                pos = (self.sprite.x - self.dir * 64 , self.sprite.y - 16)
                self.world.entities.append(gameplay.entity.Boomerang(self, pos))
            if self.animation.timer == 40:
                self.state = "idle"

        if self.state == "cyclone":
            if self.animation.timer == 32:
                self.dir = random.choice((-1, 1))
                self.sprite.x = 816 - 378 * self.dir
                self.sprite.y = 384
            if self.animation.timer == 88:
                pos = (self.sprite.x + 72 * self.dir, 400)
                self.world.entities.append(gameplay.entity.Cyclone(self.world, pos, self.dir))
            if self.animation.timer == 136:
                self.invincibility = 0
                self.dir = random.choice([-1, 1])
                self.sprite.x = 725 + random.random() * 200
                self.sprite.y = 64
            if self.animation.timer == 168:
                self.state = "idle"

        if self.state == "hurt":
            if self.animation.timer == 320:
                self.world.entities.append(gameplay.entity.HalfMoon((self.sprite.x + 64, self.sprite.y), 1))
                self.world.entities.append(gameplay.entity.HalfMoon((self.sprite.x - 64, self.sprite.y), -1))

                self.yVel = -3

            if self.animation.timer >= 424:
                self.dir = random.choice([-1, 1])
                self.boomerangTimer = random.randint(150, 300)
                self.cycloneTimer = random.randint(300, 450)
                self.state = "idle"

                if abs(self.sprite.x - 816) > 328 \
                and cmp(self.sprite.x, 816) == self.dir:
                    self.dir *= -1

                self.animation.timer = 0

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter + 32) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 33) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if entity.invincibility <= 0:
                if self.health > 0 and self.invincibility <= 0:
                    if self.sprite.collidesWith(entity.sprite):
                        entity.getHurt(self)

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.state == "hurt" and not self.onSurface():
            if self.animation.timer < 320:
                self.sprite.x = int(self.sprite.x)
                self.yVel = min(self.yVel + 0.5, 6)

            self.xVel *= 0.98
        else: self.xVel *= 0.9

        if self.yVel < 0 and self.sprite.y <= 72:
            self.yVel *= 0.5
