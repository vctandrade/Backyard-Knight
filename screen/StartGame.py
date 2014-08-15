import screen
import graphics
import data

class StartGame(object):

    def __init__(self):
        self.startgame_list = graphics.userInterface.Interface()

        self.startgame_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.2)
        self.startgame_list.addButton(1, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4)
        self.startgame_list.addButton(2, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6)
        self.startgame_list.addButton(3, "button.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1)

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
