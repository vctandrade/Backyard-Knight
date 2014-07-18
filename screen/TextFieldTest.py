import pygame
import graphics

class TextFieldTest(object):

    def __init__(self):
        self.tf = graphics.userInterface.TextField("textField.png", 380, 320)
        pass

    def displayOutput(self, display):
        display.blit(self.tf.getIcon(), self.tf.getDrawPos())

        pass

    def respondToUserInput(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.tf.updateHover(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.tf.clickDown()
        if event.type == pygame.MOUSEBUTTONUP:
            self.tf.clickUp()

        self.tf.inputText(event)

        return self

    def update(self):
        pass
