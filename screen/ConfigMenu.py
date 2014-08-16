import screen
import data
import graphics
import pygame

class ConfigMenu(object):

    def __init__(self):
        pygame.mixer.music.load("theday.xm")
        pygame.mixer.music.play()

        self.configMenu_list = graphics.userInterface.Interface()
        self.resolutions_strings = ["1024x768", "1280x768", "1600x900", "1920x1080"]
        self.resolutions = [(1024, 768), (1280, 768), (1600, 900), (1920, 1080)]
        self.index = self.resolutions.index((data.config.WIDTH, data.config.HEIGHT))

        self.configMenu_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.configMenu_list.addButton(1, "arrow_left.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6, mask="arrow_leftMask.png")
        self.configMenu_list.addButton(2, "arrow_right.png", data.config.WIDTH * 0.9, data.config.HEIGHT * 0.6, mask="arrow_rightMask.png")
        self.configMenu_list.addSlider("musicVolume", "slider.png", "slidermask.png", (0, 100), data.config.MUSIC, data.config.WIDTH * 0.7 , data.config.HEIGHT * 0.3)
        self.configMenu_list.addSlider("musicSound", "slider.png", "slidermask.png", (0, 100), data.config.SOUND, data.config.WIDTH * 0.7 , data.config.HEIGHT * 0.4)

    def displayOutput(self, display):
        display.blit(data.getResource("castle.jpg"), graphics.drawPos(0, 0))
        self.configMenu_list.draw(display)
        graphics.drawText(display, self.resolutions_strings[self.index], data.config.WIDTH * 0.7, data.config.HEIGHT * 0.6, size=24, formatting="center")
        graphics.drawText(display, data.translate("resolution"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.6, size=24, formatting="center")
        graphics.drawText(display, data.translate("music"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.3, size=24, formatting="center")
        graphics.drawText(display, data.translate("sound"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.4, size=24, formatting="center")
        graphics.drawText(display, data.translate("volume"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.2, size=24, formatting="center")

    def respondToUserInput(self, event):
        for e in self.configMenu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    data.config.WIDTH, data.config.HEIGHT = self.resolutions[self.index]
                    pygame.display.set_mode(self.resolutions[self.index])
                    data.saveConfig()
                    return screen.Menu()
                if e.button == 1:
                    self.index -= 1
                if e.button == 2:
                    self.index += 1

                self.index = self.index % len(self.resolutions)

        data.config.MUSIC = self.configMenu_list.getSliderValue("musicVolume")
        data.config.SOUND = self.configMenu_list.getSliderValue("musicSound")

        pygame.mixer.music.set_volume(data.config.MUSIC / 100.0)

        return self

    def update(self):
        pass
