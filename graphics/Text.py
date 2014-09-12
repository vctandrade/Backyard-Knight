import pygame
import data

def drawText(display, string, x, y, color=0x262626, size=10, formatting="left", font="Potash_10x10.png"):

    font = data.getResource(font)
    begin = size * len(string) / 2 if formatting == "center" else 0

    for c in string:
        c = ord(c.encode("cp437", "replace"))
        pixelarray = pygame.PixelArray(font[c].copy())
        for i in range(len(pixelarray)):
            for j in range(len(pixelarray[i])):
                if pixelarray[i][j] == 0xFFFFFF:
                    pixelarray[i][j] = color

        char = pixelarray.make_surface()
        char = pygame.transform.scale(char, (size, size))
        char.set_colorkey(0xFF00FF)
        display.blit(char, (x - begin, y - size / 2))

        x += size
