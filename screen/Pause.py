import screen
import graphics
import pygame
import data

class Pause(object):

    def __init__(self):

        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.3, data.config.HEIGHT * 0.5)
        self.menu_list.addButton(2, "button.png", data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5)
        self.menu_list.addButton(3, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7)

    def displayOutput(self, display):
        resolution = (data.config.WIDTH, data.config.HEIGHT)
        shadow = pygame.Surface(resolution, pygame.SRCALPHA)
        shadow.fill((0, 0, 0, 128))
        display.blit(shadow, (0, 0))

        self.menu_list.draw(display)

        graphics.drawText(display, data.translate("return"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3, size=20 , formatting="center")
        graphics.drawText(display, data.translate("help"), data.config.WIDTH * 0.3, data.config.HEIGHT * 0.5, size=20 , formatting="center")
        graphics.drawText(display, data.translate("configurations"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5, size=20 , formatting="center")
        graphics.drawText(display, data.translate("exit"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7, size=20 , formatting="center")

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    return None
                if e.button == 1:
                    return screen.Help(self.__class__)
                if e.button == 2:
                    return screen.ConfigMenu(self.__class__)
                if e.button == 3:
                    return screen.Menu()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return None

        return self

    def update(self):
        pass
