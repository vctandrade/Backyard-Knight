import graphics
import pygame
import data

class CheckBox(object):

    def __init__(self, icon, x, y, checked=False, active=True, visible=True, mask=None):

        self.icon = icon
        self.mask = mask

        self.width = data.getResource(icon).width
        self.height = data.getResource(icon).height

        self.x = x
        self.y = y

        self.active = active
        self.visible = visible

        self.checked = checked

        self.hovered = False
        self.clicked = False

    def getIcon(self):
        if not self.visible: return graphics.blankImage

        index = 0 if not self.checked else 1
        index += 0 if self.active else 2

        return data.getResource(self.icon)[index]

    def getDrawPos(self):
        return [(self.x - self.width / 2, self.y - self.height / 2), (0, 0)]

    def updateHover(self):
        pos = pygame.mouse.get_pos()

        x = pos[0] - int(self.x - self.width / 2)
        y = pos[1] - int(self.y - self.height / 2)

        mask = data.getResource(self.mask)

        if 0 <= x < self.width and 0 <= y < self.height \
        and (mask == None or mask[x][y] == 0xFF):
                self.hovered = True

        else:
            self.hovered = False
            self.clicked = False

        return self.hovered if self.active else False

    def clickDown(self):
        if self.hovered: self.clicked = True

    def clickUp(self):
        if self.clicked and self.hovered and self.active:
            self.clicked = False
            self.checked = not self.checked

        else: self.clicked = False

    def __setattr__(self, name, value):
        self.__dict__[name] = value

        if self.__dict__.has_key('clicked'):
            if name == 'x' or name == 'y':
                self.updateHover(pygame.mouse.get_pos())
