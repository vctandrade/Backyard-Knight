import graphics
import random

class Bone(object):

    def __init__(self, index, pos, side):

        self.xVel = 2.5 - 5 * random.random()
        self.yVel = -2 - 3 * random.random()

        torque = random.random() * 10 * cmp(0, self.xVel)

        self.animation = graphics.AnimationInfo()
        self.animation.angle = lambda: torque * self.animation.timer
        self.animation.alpha = lambda: 512 - self.animation.timer * 256 / 20.0

        self.sprite = graphics.Sprite(index, "skeleton.png", pos)
        self.sprite.xScale = side

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel
        self.sprite.y += self.yVel

        if self.animation.timer >= 40:
            self.dead = True

        self.applyGravity()

    def applyGravity(self):
        self.yVel = self.yVel + 0.3
