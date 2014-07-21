import pygame
import Events

from Button import Button
from CheckBox import CheckBox

class Interface(object):

    def __init__(self):
        self.buttons = list()
        self.checkBoxes = dict()

    def addButton(self, index, iconPath, x, y, active=True, visible=True, mask=None):
        newButton = Button(index, iconPath, x, y, active, visible, mask)
        newButton.updateHover()

        self.buttons.append(newButton)

    def addCheckBox(self, tag, iconPath, x, y, checked=False, active=True, visible=True, mask=None):
        newCheckBox = CheckBox(iconPath, x, y, checked, active, visible, mask)
        newCheckBox.updateHover()

        self.checkBoxes[tag] = newCheckBox

    def boxChecked(self, tag):
        return self.checkBoxes[tag].checked

    def handle(self, event):
        output = list()

        hoverMode = Events.NOHOVER

        for i in self.buttons + self.checkBoxes.values():
            if i.updateHover(): hoverMode = Events.CLICKHOVER

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.buttons + self.checkBoxes.values():
                i.clickDown()

        if event.type == pygame.MOUSEBUTTONUP:
            for b in self.buttons:
                if b.clickUp(): output.append(Events.ButtonClicked(b.index))

            for cb in self.checkBoxes.values():
                cb.clickUp()

        output.append(Events.Hover(hoverMode))

        return output

    def draw(self, display):
        for b in self.buttons:
            display.blit(b.getIcon(), b.getDrawPos())

        for cb in self.checkBoxes.values():
            display.blit(cb.getIcon(), cb.getDrawPos())
