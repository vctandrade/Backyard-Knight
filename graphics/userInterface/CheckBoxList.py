from CheckBox import CheckBox
import pygame

class CheckBoxList(object):

    def __init__(self):
        self.checkBoxes = dict()

    def __getitem__(self, i):
        return self.checkBoxes[i]

    def isChecked(self, tag):
        return self.checkBoxes[tag].checked

    def add(self, tag, iconPath, x, y, checked=False, active=True, visible=True, mask=None):
        newCheckBox = CheckBox(iconPath, x, y, checked, active, visible, mask)
        newCheckBox.updateHover(pygame.mouse.get_pos())

        self.checkBoxes[tag] = newCheckBox

    def handle(self, event):

        if event.type == pygame.MOUSEMOTION:
            for cb in self.checkBoxes.values():
                cb.updateHover(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for cb in self.checkBoxes.values():
                cb.clickDown()

        if event.type == pygame.MOUSEBUTTONUP:
            for cb in self.checkBoxes.values():
                cb.clickUp()

    def draw(self, display):
        for cb in self.checkBoxes.values():
            display.blit(cb.getIcon(), cb.getDrawPos())
