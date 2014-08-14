import screen
import graphics
import data

class StartGame(object):

    def __init__(self):
        self.startgame_list = graphics.userInterface.Interface()

        button_width = data.getResource("button.png").width
        button_height = data.getResource("button.png").height

        self.startgame_list.addButton(0, "button.png", data.config.WIDTH * 0.5 - (button_width) / 2, data.config.HEIGHT * 0.2 - (button_height) / 2)
        self.startgame_list.addButton(1, "button.png", data.config.WIDTH * 0.5 - (button_width) / 2, data.config.HEIGHT * 0.4 - (button_height) / 2)
        self.startgame_list.addButton(2, "button.png", data.config.WIDTH * 0.5 - (button_width) / 2, data.config.HEIGHT * 0.6 - (button_height) / 2)
        self.startgame_list.addButton(3, "button.png", data.config.WIDTH * 0.1 - (button_width) / 2, data.config.HEIGHT * 0.1 - (button_height) / 2)

    def displayOutput(self, display):
        self.startgame_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.startgame_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 3:
                    return screen.Menu()
        return self

    def update(self):
        pass
