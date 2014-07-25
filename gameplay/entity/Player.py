import pygame
import graphics

class Player(object):

    def __init__(self, world):
        self.world = world
        self.xVel, self.yVel = (0, 0)
        self.sprite = graphics.Sprite(0, "bob.png", (0, 0))
        self.animation = graphics.AnimationInfo()
        self.state = "idle"

    def draw(self, display, offset=(0, 0)):
        if self.xVel > 0: self.sprite.xScale = 1
        if self.xVel < 0: self.sprite.xScale = -1

        if self.onSurface():
            if self.state == "walking":
                self.animation.set(index=lambda: (self.animation.timer % 8) / 4)
            else: self.animation.set(index=lambda: 0)
        else: self.animation.set(index=lambda: 2)

        self.animation.animate(self.sprite)

        self.sprite.draw(display, offset)

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: self.moveRight()
            if event.key == pygame.K_a: self.moveLeft()
            if event.key == pygame.K_SPACE: self.jump()

    def moveLeft(self):
        self.xVel = max(self.xVel - 1, -5)
        self.state = "walking"

    def moveRight(self):
        self.xVel = min(self.xVel + 1, 5)
        self.state = "walking"

    def jump(self):
        if self.onSurface():
            self.yVel = -10

    def update(self):
        self.state = "idle"
        self.animation.timer += 1

        self.sprite.x += self.xVel

        if self.collided():
            if self.xVel >= 0: self.sprite.x -= (self.sprite.x + self.sprite.xCenter - 10) % 64
            else: self.sprite.x += 64 - (self.sprite.x - self.sprite.xCenter + 10) % 64

            self.xVel = 0

        self.applyGravity()

        self.sprite.y += self.yVel

        if self.collided():
            if self.yVel >= 0: self.sprite.y -= (self.sprite.y + self.sprite.yCenter) % 64
            else: self.sprite.y += 64 - (self.sprite.y - self.sprite.yCenter + 10) % 64

            self.yVel = 0

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter + 10) / 64
        r = int(self.sprite.x + self.sprite.xCenter - 1 - 10) / 64

        t = int(self.sprite.y - self.sprite.yCenter + 10) / 64
        b = int(self.sprite.y + self.sprite.yCenter - 1) / 64

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map.map[y][x].isColidable():
                    return True

        return False

    def onSurface(self):
        self.sprite.y += 1
        check = self.collided()
        self.sprite.y -= 1
        return check

    def applyGravity(self):
        if self.onSurface(): self.xVel *= 0.8
        else: self.yVel = min(self.yVel + 0.5, 64)
