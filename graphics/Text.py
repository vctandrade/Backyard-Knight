import pygame
import data

fontList = {}

def drawText(display, string, x, y, color=0x262626, size=10, formatting="left", font="Potash_10x10.png"):

    index = (color, size, font)
    begin = size * len(string) / 2 if formatting == "center" else 0

    if index not in fontList:
        font = data.getResource(font).copy()

        for k, char in enumerate(font):
            char = pygame.PixelArray(char)

            for i, line in enumerate(char):
                for j, pixel in enumerate(line):
                    if pixel == 0xFFFFFF:
                        char[i][j] = color

            char = char.make_surface()
            char.set_colorkey(0xFF00FF)
            font[k] = pygame.transform.scale(char, (size, size))

        fontList[index] = font

    for char in string:
        char = ord(char.encode("cp437", "replace"))
        display.blit(fontList[index][char], (x-begin, y-size/2))
        x += size
