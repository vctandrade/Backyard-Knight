import graphics
import pygame
import data

class Slider(object):

    def __init__(self, icon, mask, boundaries, default, x, y, vertical=False, active=True, visible=True):

        self.value = default
        self.left, self.right = boundaries

        self.icon = icon
        self.mask = mask

        self.width = data.getResource(icon).width
        self.height = data.getResource(icon).height

        self.threshold = int(self.width * 0.06)

        self.vertical = vertical

        self.x = x
        self.y = y

        self.active = active
        self.visible = visible

        self.hovered = False
        self.clicked = False

    def getPos(self):
        return (self.width - 2 * self.threshold) * (self.value - self.left) / (self.right - self.left) + self.threshold

    def setPos(self, x):
        self.value = (x - self.threshold) * (self.right - self.left) / (self.width - 2 * self.threshold) + self.left

    def getIcon(self):
        if not self.visible: return graphics.blankImage

        index = 0
        if not self.active:
            index = 2

        icon = data.getResource(self.icon)[index + 1].copy()
        icon.blit(data.getResource(self.icon)[index], (self.getPos() - self.width / 2, 0))

        if self.vertical: icon = pygame.transform.rotate(icon, -90)

        return icon

    def getDrawPos(self):
        return [(self.x, self.y), (0, 0)]

    def updateHover(self):
        if not self.active:
            self.hovered = False
            self.clicked = False
            return

        pos = pygame.mouse.get_pos()

        x = pos[0] - (self.x - self.width / 2 + self.getPos())
        y = pos[1] - self.y

        if self.vertical:
            x = pos[1] - (self.y - self.width / 2 + self.getPos())
            y = self.height - (pos[0] - self.x)

        mask = data.getResource(self.mask)

        if 0 <= x < self.width and 0 <= y < self.height \
        and  mask[x][y] == 0xFF: self.hovered = True

        else: self.hovered = False

        if self.clicked:
            x -= self.width / 2 - self.getPos() - (self.width - 2 * self.threshold) / (self.right - self.left) / 2
            self.setPos(max(self.threshold, min(x, self.width - self.threshold)))

        return self.active and (self.hovered or self.clicked)

    def clickDown(self):
        if self.hovered: self.clicked = True

    def clickUp(self):
        self.clicked = False

    def __setattr__(self, name, value):
        self.__dict__[name] = value

        if self.__dict__.has_key('clicked'):
            if name == 'x' or name == 'y':
                self.updateHover(pygame.mouse.get_pos())
