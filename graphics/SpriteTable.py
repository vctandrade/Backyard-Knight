import pygame

class SpriteTable(object):

    def __init__(self, imgPath, width=1, height=1):
        uncutTable = pygame.image.load(imgPath)

        uncutWidth = uncutTable.get_width() * 2
        uncutHeight = uncutTable.get_height() * 2

        uncutTable = pygame.transform.scale(uncutTable, (uncutWidth, uncutHeight))

        width = uncutWidth / width
        height = uncutHeight / height

        self.width = width
        self.height = height

        self.table = list()

        j = 0
        while j < uncutHeight:
            i = 0
            while i < uncutWidth:
                self.table.append(pygame.Surface((width, height)))
                self.table[-1].blit(uncutTable, (0, 0), [(i, j), (width, height)])

                self.table[-1].set_colorkey(0xFF00FF, pygame.RLEACCEL)

                i += width
            j += height

    def __getitem__(self, i):
        return self.table[i]

    def copy(self):
        return [sprite.copy() for sprite in self.table]
