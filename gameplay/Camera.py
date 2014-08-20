import data
import random

class Camera(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.shake = 0
        self.decay = 0

    def convert(self):
        return self.x, self.y

    def setShake(self, magnitude, decay):
        self.shake = magnitude
        self.decay = decay

    def update(self, focus):
        x0 = focus.x - data.config.WIDTH / 2
        y0 = focus.y - data.config.HEIGHT / 2

        x0 += random.random() * self.shake - self.shake / 2
        y0 += random.random() * self.shake - self.shake / 2

        self.shake *= self.decay

        if abs(self.x - x0) > 8:
            self.x += (x0 - self.x) / 32

        if abs(self.y - y0) > 8:
            self.y += (y0 - self.y) / 32
