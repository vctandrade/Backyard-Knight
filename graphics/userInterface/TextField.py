import data
import graphics
import pygame

class TextField(object):

    def __init__(self, image, x, y, color=0xFFFFFF, size=16, text="asd", focused=False, active=True, visible=True, mask=None):

        self.image = image
        self.mask = mask

        self.color = color
        self.size = size

        self.text = text
        self.pos = 0

        self.width = data.getResource(image).get_width()
        self.height = data.getResource(image).get_height()

        self.x = x
        self.y = y

        self.active = active
        self.visible = visible

        self.hovered = False
        self.clicked = False

        self.focused = focused

        self.tick = 0

    def getIcon(self):
        if not self.visible: return graphics.blankImage

        icon = data.getResource(self.image).copy()
        graphics.drawText(icon, self.text, self.width * 0.06, self.height / 2 - self.size / 2, self.color, self.size)

        if (self.tick / 24) % 2 == 0 and self.focused:
            graphics.drawText(icon, "|", self.width * 0.06 + (self.pos - 0.5) * self.size - 3, self.height / 2 - (self.size + 8) / 2, 0x000000, self.size + 8)
        self.tick += 1

        return icon

    def getDrawPos(self):
        return [(self.x, self.y), (0, 0)]

    def updateHover(self):
        pos = pygame.mouse.get_pos()

        x = pos[0] - self.x
        y = pos[1] - self.y

        mask = data.getResource(self.mask)

        if 0 <= x < self.width and 0 <= y < self.height \
        and (mask == None or mask[x][y] == 0xFF):
                self.hovered = True

        else:
            self.hovered = False
            self.clicked = False

        return self.hovered if self.active else False

    def clickDown(self):
        if self.hovered:
            self.clicked = True

            newPos = (pygame.mouse.get_pos()[0] - self.width * 0.06 - self.x) / self.size
            self.pos = max(0, min(int(round(newPos)), len(self.text)))

            self.tick = 0

    def clickUp(self):
        if self.clicked and self.hovered and self.active:
            self.clicked = False
            self.focused = True

        else:
            self.focused = False
            self.clicked = False

    def inputText(self, event):
        if event.type != pygame.KEYDOWN or not self.focused or not self.active:
            return

        if " " <= event.unicode <= "~":
            if len(self.text) * self.size < self.width * 0.88:
                self.text = self.text[:self.pos] + event.unicode + self.text[self.pos:]
                self.pos += 1

        if event.key == pygame.K_BACKSPACE:
            if self.pos > 0:
                self.text = self.text[:self.pos - 1] + self.text[self.pos:]
                self.pos -= 1

        if event.key == pygame.K_DELETE:
            if self.pos < len(self.text):
                self.text = self.text[:self.pos] + self.text[self.pos + 1:]

        if event.key == pygame.K_HOME:
            self.pos = 0

        if event.key == pygame.K_END:
            self.pos = len(self.text)

        if event.key == pygame.K_RIGHT:
            if self.pos < len(self.text):
                self.pos += 1

        if event.key == pygame.K_LEFT:
            if self.pos > 0: self.pos -= 1

        self.tick = 0

    def __setattr__(self, name, value):
        self.__dict__[name] = value

        if self.__dict__.has_key('clicked'):
            if name == 'x' or name == 'y':
                self.updateHover(pygame.mouse.get_pos())
