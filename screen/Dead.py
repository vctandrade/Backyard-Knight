import screen
import graphics
import pygame
import data

class Dead(object):

    def __init__(self):

        self.transitionTimer = 0

        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7)

    def displayOutput(self, display):
        resolution = (data.config.WIDTH, data.config.HEIGHT)

        buff = pygame.Surface(resolution, pygame.SRCALPHA)
        shadow = pygame.Surface(resolution, pygame.SRCALPHA)
        shadow.fill((255 - self.transitionTimer * 2, 0, 0, self.transitionTimer))
        buff.blit(shadow, (0, 0))

        self.menu_list.draw(buff)

        graphics.drawText(buff, data.translate("menu"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3, size=20 , formatting="center")
        graphics.drawText(buff, data.translate("restart"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7, size=20 , formatting="center")

        display.blit(buff, (0, 0))
        self.transitionTimer = min(self.transitionTimer + 1, 127)
    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    pass
                if e.button == 1:
                    pass

        return self

    def update(self):
        pass
