import screen
import graphics
import pygame
import data

class Menu(object):

    def __init__(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("theday.xm")
            pygame.mixer.music.set_volume(data.config.MUSIC / 100.0)
            pygame.mixer.music.play()

        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.9)
        self.menu_list.addButton(2, "button.png", data.config.WIDTH * 0.3, data.config.HEIGHT * 0.9)
        self.menu_list.addButton(3, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.9)
        self.menu_list.addButton(4, "button.png", data.config.WIDTH * 0.7, data.config.HEIGHT * 0.9)
        self.menu_list.addButton(5, "button.png", data.config.WIDTH * 0.9, data.config.HEIGHT * 0.9)

    def displayOutput(self, display):
        display.blit(data.getResource("windows_xp.png"), (0, 0))
        display.blit(data.getResource("logo.png"), (data.config.WIDTH * 0.5 - 461, data.config.HEIGHT * 0.05))
        self.menu_list.draw(display)

        graphics.drawText(display, data.translate("start"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6, size=20 , formatting="center")
        graphics.drawText(display, data.translate("help"), data.config.WIDTH * 0.1, data.config.HEIGHT * 0.9, size=20 , formatting="center")
        graphics.drawText(display, data.translate("ranking"), data.config.WIDTH * 0.3, data.config.HEIGHT * 0.9, size=20 , formatting="center")
        graphics.drawText(display, data.translate("configurations"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.9, size=20 , formatting="center")
        graphics.drawText(display, data.translate("credits"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.9, size=20 , formatting="center")
        graphics.drawText(display, data.translate("exit"), data.config.WIDTH * 0.9, data.config.HEIGHT * 0.9, size=20 , formatting="center")

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    return screen.StartGame()
                if e.button == 1:
                    return screen.Help(self)
                if e.button == 2:
                    return screen.Ranking()
                if e.button == 3:
                    return screen.ConfigMenu(self)
                if e.button == 4:
                    return screen.Credits()
                if e.button == 5:
                    return  None

        return self

    def update(self):
        pass
