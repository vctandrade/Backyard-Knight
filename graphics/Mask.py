import pygame
import data

class Mask(object):

    def __init__(self, maskPath):
        image = data.loadImage(maskPath)

        pixelArray = pygame.PixelArray(image)

        width = len(pixelArray)
        height = len(pixelArray[0])

        self.mask = [list() for i in range(width)]

        for x in range(width):
            for y in range(height):
                self.mask[x].append(pixelArray[x][y] % 0x100)

    def __getitem__(self, i):
        return self.mask[i]
