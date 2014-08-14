import screen
import data
import graphics

class ConfigMenu(object):

    def __init__(self):
        self.configMenu_list = graphics.userInterface.Interface()

        button_width = data.getResource("button.png").width
        button_height = data.getResource("button.png").height

        slider_width = data.getResource("slider.png").width
        slider_height = data.getResource("slider.png").height

        self.configMenu_list.addButton(0, "button.png", data.config.WIDTH * 0.1 - (button_width) / 2 , data.config.HEIGHT * 0.1 - (button_height) / 2)
        self.configMenu_list.addSlider("musicVolume", "slider.png", "slidermask.png", (0, 100), data.config.MUSIC, int(data.config.WIDTH * 0.7 - (slider_width) / 2) , int(data.config.HEIGHT * 0.3 - (slider_height) / 2))
        self.configMenu_list.addSlider("musicSound", "slider.png", "slidermask.png", (0, 100), data.config.SOUND, int(data.config.WIDTH * 0.7 - (slider_width) / 2) , int(data.config.HEIGHT * 0.4 - (slider_height) / 2))

    def displayOutput(self, display):
        self.configMenu_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.configMenu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    data.saveConfig()
                    return screen.Menu()

        data.config.MUSIC = self.configMenu_list.getSliderValue("musicVolume")
        data.config.SOUND = self.configMenu_list.getSliderValue("musicSound")

        return self

    def update(self):
        pass
