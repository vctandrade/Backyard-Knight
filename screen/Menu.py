import screen
import graphics
import data

class Menu(object):

    def __init__(self):
        self.menu_list = graphics.userInterface.Interface()

        button_width = data.getResource("button.png").width
        button_height = data.getResource("button.png").height

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5 - (button_width) / 2, data.config.HEIGHT * 0.5 - (button_height) / 2)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.1 - (button_width) / 2, data.config.HEIGHT * 0.91 - (button_height) / 2)
        self.menu_list.addButton(2, "button.png", data.config.WIDTH * 0.3 - (button_width) / 2, data.config.HEIGHT * 0.91 - (button_height) / 2)
        self.menu_list.addButton(3, "button.png", data.config.WIDTH * 0.5 - (button_width) / 2, data.config.HEIGHT * 0.91 - (button_height) / 2)
        self.menu_list.addButton(4, "button.png", data.config.WIDTH * 0.7 - (button_width) / 2, data.config.HEIGHT * 0.91 - (button_height) / 2)
        self.menu_list.addButton(5, "button.png", data.config.WIDTH * 0.9 - (button_width) / 2, data.config.HEIGHT * 0.91 - (button_height) / 2)

    def displayOutput(self, display):
        display.blit(data.getResource("help_image1.png"), (400, 200))
        self.menu_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    return screen.StartGame()
                if e.button == 1:
                    return screen.Help()
                if e.button == 2:
                    return screen.Ranking()
                if e.button == 3:
                    return screen.ConfigMenu()
                if e.button == 4:
                    return screen.Credits()
                if e.button == 5:
                    return  None

        return self

    def update(self):
        pass
