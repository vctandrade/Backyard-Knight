import pygame
import Events

from Button import Button
from CheckBox import CheckBox
from Slider import Slider
from TextField import TextField

class Interface(object):

    def __init__(self):
        self.buttons = list()
        self.checkBoxes = dict()
        self.sliders = dict()
        self.textFields = dict()

    def addButton(self, index, iconPath, x, y, active=True, visible=True, mask=None):
        newButton = Button(index, iconPath, x, y, active, visible, mask)
        newButton.updateHover()

        self.buttons.append(newButton)

    def addCheckBox(self, tag, iconPath, x, y, checked=False, active=True, visible=True, mask=None):
        newCheckBox = CheckBox(iconPath, x, y, checked, active, visible, mask)
        newCheckBox.updateHover()

        self.checkBoxes[tag] = newCheckBox

    def addSlider(self, tag, icon, mask, boundaries, default, x, y, vertical=False, active=True, visible=True):
        newSlider = Slider(icon, mask, boundaries, default, x, y, vertical, active, visible)
        newSlider.updateHover()

        self.sliders[tag] = newSlider

    def addTextField(self, tag, image, x, y, color=0xFFFFFF, size=16, text="", focused=False, active=True, visible=True, mask=None):
        newTextField = TextField(image, x, y, color, size, text, focused, active, visible, mask)
        newTextField.updateHover()

        self.textFields[tag] = newTextField

    def boxChecked(self, tag):
        return self.checkBoxes[tag].checked

    def getSliderValue(self, tag):
        return self.sliders[tag].value

    def getText(self, tag):
        return self.textFields[tag].text

    def handle(self, event):
        output = list()

        for tf in self.textFields.values():
            tf.inputText(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in self.buttons + self.checkBoxes.values() + self.sliders.values() + self.textFields.values():
                i.clickDown()

        if event.type == pygame.MOUSEBUTTONUP:
            for b in self.buttons:
                if b.clickUp(): output.append(Events.ButtonClicked(b.index))

            for cb in self.checkBoxes.values():
                cb.clickUp()

            for s in self.sliders.values():
                s.clickUp()

            for tf in self.textFields.values():
                tf.clickUp()

        hoverMode = Events.NOHOVER

        for i in self.buttons + self.checkBoxes.values() + self.sliders.values():
            if i.updateHover(): hoverMode = Events.CLICKHOVER

        for i in self.textFields.values():
            if i.updateHover(): hoverMode = Events.TEXTHOVER

        output.append(Events.Hover(hoverMode))

        return output

    def draw(self, display):
        for b in self.buttons:
            display.blit(b.getIcon(), b.getDrawPos())

        for cb in self.checkBoxes.values():
            display.blit(cb.getIcon(), cb.getDrawPos())

        for s in self.sliders.values():
            display.blit(s.getIcon(), s.getDrawPos())

        for tf in self.textFields.values():
            display.blit(tf.getIcon(), tf.getDrawPos())
