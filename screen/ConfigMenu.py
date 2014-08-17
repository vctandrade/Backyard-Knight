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
        self.resolution_index = self.resolutions.index((data.config.WIDTH, data.config.HEIGHT))
        
        self.languages_strings = [data.translate("english"), data.translate("portuguese")]
        self.languages = ["en_us","pt_br"]
        self.language_index = self.languages.index(data.config.LANG)
        
        slider_width = data.getResource("slider.png").width
        slider_height = data.getResource("slider.png").height

        self.configMenu_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        
        self.configMenu_list.addButton(1, "pointer_left.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6, mask="pointer_leftMask.png")
        self.configMenu_list.addButton(2, "pointer_right.png", data.config.WIDTH * 0.9, data.config.HEIGHT * 0.6, mask="pointer_rightMask.png")
        
        self.configMenu_list.addButton(3, "pointer_left.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.8, mask="pointer_leftMask.png")
        self.configMenu_list.addButton(4, "pointer_right.png", data.config.WIDTH * 0.9, data.config.HEIGHT * 0.8, mask="pointer_rightMask.png")
        
        self.configMenu_list.addSlider("musicVolume", "slider.png", "slidermask.png", (0, 100), data.config.MUSIC, int(data.config.WIDTH * 0.7 - (slider_width) / 2) , int(data.config.HEIGHT * 0.3 - (slider_height) / 2))
        self.configMenu_list.addSlider("musicSound", "slider.png", "slidermask.png", (0, 100), data.config.SOUND, int(data.config.WIDTH * 0.7 - (slider_width) / 2) , int(data.config.HEIGHT * 0.4 - (slider_height) / 2))

    def displayOutput(self, display):
        display.blit(data.getResource("castle.jpg"), graphics.drawPos(0, 0))
        self.configMenu_list.draw(display)
       
    
        graphics.drawText(display, data.translate("configurations"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1,formatting = "center",size = 40)
        graphics.drawText(display, data.translate("resolution"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.6, size=24, formatting="center")
        graphics.drawText(display, data.translate("music"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.3, size=24, formatting="center")
        graphics.drawText(display, data.translate("sound"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.4, size=24, formatting="center")
        graphics.drawText(display, data.translate("volume"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.2, size=24, formatting="center")
        graphics.drawText(display, data.translate("language"), data.config.WIDTH * 0.2, data.config.HEIGHT * 0.8, size=24, formatting="center")
        
        graphics.drawText(display, self.resolutions_strings[self.resolution_index], data.config.WIDTH * 0.7, data.config.HEIGHT * 0.6, size=24, formatting="center")
        graphics.drawText(display, self.languages_strings[self.language_index], data.config.WIDTH * 0.7, data.config.HEIGHT * 0.8, size=24, formatting="center")

    def respondToUserInput(self, event):
        for e in self.configMenu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    data.config.WIDTH, data.config.HEIGHT = self.resolutions[self.resolution_index]
                    data.config.LANG = self.languages[self.language_index]
                    pygame.display.set_mode(self.resolutions[self.resolution_index])
                    
                    data.saveConfig()
                    data.loadLanguage()
                    return screen.Menu()
                if e.button == 1:
                    self.resolution_index -= 1
                if e.button == 2:
                    self.resolution_index += 1
                if e.button == 3:
                    self.language_index -= 1
                if e.button == 4:
                    self.language_index += 1
                
                self.resolution_index = self.resolution_index % len(self.resolutions)
                self.language_index = self.language_index % 2

        data.config.MUSIC = self.configMenu_list.getSliderValue("musicVolume")
        data.config.SOUND = self.configMenu_list.getSliderValue("musicSound")

        pygame.mixer.music.set_volume(data.config.MUSIC / 100.0)

        return self

    def update(self):
        pass
