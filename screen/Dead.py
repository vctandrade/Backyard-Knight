import screen
import graphics
import pygame
import data

class Dead(object):

    def __init__(self):
        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.35, data.config.HEIGHT * 0.7)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.65, data.config.HEIGHT * 0.7)

        self.transitionTimer = 0

        resolution = data.config.WIDTH, data.config.HEIGHT
        self.redness = pygame.Surface(resolution)
        self.redness.fill((64, 0, 0))

    def displayOutput(self, display):
        resolution = data.config.WIDTH, data.config.HEIGHT

        self.redness.set_alpha(self.transitionTimer)
        display.blit(self.redness, (0, 0))

        buff = pygame.Surface(resolution)
        buff.set_alpha(self.transitionTimer * 2 + 1)
        self.menu_list.draw(buff)

        graphics.drawText(buff, data.translate("menu"), data.config.WIDTH * 0.35, data.config.HEIGHT * 0.7, size=20 , formatting="center")
        graphics.drawText(buff, data.translate("restart"), data.config.WIDTH * 0.65, data.config.HEIGHT * 0.7, size=20 , formatting="center")
        graphics.drawText(buff, "Game Over", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4, size=40 , color=0xFFFFFF, formatting="center")

        display.blit(buff, (0, 0))
        self.transitionTimer = min(self.transitionTimer + 1, 128)

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    return screen.Menu()
                if e.button == 1:
                    return screen.Gameplay()

        return self

    def update(self):
        pass
