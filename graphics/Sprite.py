import pygame
import data
import math

class Sprite(object):

    def __init__(self, index, table, pos):
        self.index = index
        self.table = table

        img = data.getResource(table)

        self.pixelArray = pygame.PixelArray(img[0].copy())

        self.alpha = 255

        self.x, self.y = pos

        self.xScale = 1
        self.yScale = 1

        self.angle = 0

        self.width = img.width
        self.height = img.height

        self.xCenter = self.width / 2
        self.yCenter = self.height / 2

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
            img = pygame.transform.scale(img, (width, height))

        if self.angle % 360 != 0:
            img = pygame.transform.rotate(img, self.angle)

        if self.centerOutdated:
            cos = math.cos(math.radians(self.angle % 90))
            sin = math.sin(math.radians(self.angle % 90))

            cos2 = math.cos(math.radians(self.angle))
            sin2 = math.sin(math.radians(self.angle))

            if self.angle % 180 < 90:
                x = (cos * width + sin * height) / 2
                y = (cos * height + sin * width) / 2
            else:
                x = (cos * height + sin * width) / 2
                y = (cos * width + sin * height) / 2

            xRefinedCenter = self.xCenter * abs(self.xScale) - width / 2
            yRefinedCenter = self.yCenter * abs(self.yScale) - height / 2

            x += cos2 * xRefinedCenter - sin2 * yRefinedCenter
            y += sin2 * xRefinedCenter + cos2 * yRefinedCenter

            self.xTrueCenter, self.yTrueCenter = x, y
            self.centerOutdated = False

        x = self.x - self.xTrueCenter - math.floor(offset[0])
        y = self.y - self.yTrueCenter - math.ceil(offset[1])

        self.pixelArray = pygame.PixelArray(img.copy())

        display.blit(img, (x, y))

    def collidesWith(self, other):

        # DOESN'T WORK WITH ROTATED IMAGES!

        left = int(other.x - other.xCenter - self.x + self.xCenter)
        right = left + other.width
        up = int(other.y - other.yCenter - self.y + self.yCenter)
        down = up + other.height

        for x1 in range(max(0, left), min(right, self.width), 2):
            for y1 in range(max(0, up), min(down, self.height), 2):
                x2 = x1 + int(self.x - self.xTrueCenter - other.x + other.xTrueCenter)
                y2 = y1 + int(self.y - self.yTrueCenter - other.y + other.yTrueCenter)
                if self.pixelArray[x1][y1] != 0xFF00FF and other.pixelArray[x2][y2] != 0xFF00FF:
                    return True

        return False

    def __setattr__(self, name, value):
        if name in ("xScale", "yScale", "angle", "xCenter", "yCenter") \
        and self.__dict__.has_key(name) and self.__dict__[name] != value:
            self.centerOutdated = True
        self.__dict__[name] = value
