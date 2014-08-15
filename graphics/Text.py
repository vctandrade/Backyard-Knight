import data
import graphics
import pygame

def drawText(display, string, x, y, color=0xFFFFFF, size=16, formatting="left"):

    font = data.getResource("Cheepicus_8x8.png")

    begin = size * len(string) / 2 if formatting == "center" else 0


    for c in string:
        c = ord(c)
        pixelarray = pygame.PixelArray(font[c].copy())
        for i in range(len(pixelarray)):
            for j in range(len(pixelarray[i])):
                if pixelarray[i][j] != 0xFF00FF:
                    pixelarray[i][j] = color

        char = pixelarray.make_surface()
        char = pygame.transform.scale(char, (size, size))
        char.set_colorkey(0xFF00FF)
        display.blit(char, graphics.drawPos(x - begin, y - size / 2))
        x += size
