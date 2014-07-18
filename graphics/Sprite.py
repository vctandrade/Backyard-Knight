import graphics
import pygame
import data
import math

class Sprite(object):

    def __init__(self, index, table, pos):
        self.index = index
        self.table = table

        self.alpha = 255

        self.x, self.y = pos

        self.xScale = 1
        self.yScale = 1

        self.angle = 0

        width = data.getResource(table).width
        height = data.getResource(table).height

        self.xCenter = width / 2
        self.yCenter = height / 2

        self.xTrueCenter = self.xCenter
        self.yTrueCenter = self.yCenter

        self.centerOutdated = False

    def draw(self, display, offset=(0, 0)):
        if self.xScale == 0 or self.yScale == 0:
            return

        img = data.getResource(self.table)

        width = int(abs(self.xScale) * img.width)
        height = int(abs(self.yScale) * img.height)

        img = img[int(self.index)]
        img.set_alpha(self.alpha)

        if self.xScale < 0 or self.yScale < 0:
            img = pygame.transform.flip(img, self.xScale < 0, self.yScale < 0)

        if self.xScale != 1 or self.yScale != 1:
            img = pygame.transform.scale(img, (height, width))

        if self.angle % 360 != 0:
            img = pygame.transform.rotate(img, self.angle)

        if self.centerOutdated:
            cos = math.cos(math.radians(self.angle % 90))
            sin = math.sin(math.radians(self.angle % 90))

            cos2 = math.cos(math.radians(self.angle))
            sin2 = math.sin(math.radians(self.angle))

            if self.angle % 180 < 90:
                x = (cos * height + sin * width) / 2
                y = (cos * width + sin * height) / 2
            else:
                x = (cos * width + sin * height) / 2
                y = (cos * height + sin * width) / 2

            xRefinedCenter = self.xCenter * abs(self.xScale) - width / 2
            yRefinedCenter = self.yCenter * abs(self.yScale) - height / 2

            x += sin2 * xRefinedCenter + cos2 * yRefinedCenter
            y += cos2 * xRefinedCenter - sin2 * yRefinedCenter

            self.xTrueCenter, self.yTrueCenter = x, y
            self.centerOutdated = False

        x = self.x - self.xTrueCenter - offset[0]
        y = self.y - self.yTrueCenter - offset[1]

        display.blit(img, graphics.drawPos(x, y))

    def __setattr__(self, name, value):
        if name in ("xScale", "yScale", "angle", "xCenter", "yCenter") \
        and self.__dict__.has_key(name) and self.__dict__[name] != value:
            self.centerOutdated = True
        self.__dict__[name] = value
