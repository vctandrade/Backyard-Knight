import graphics
import screen
import data

class Ranking(object):

    def __init__(self):
        self.ranking_list = graphics.userInterface.Interface()

        button_width = data.getResource("button.png").width
        button_height = data.getResource("button.png").height

        self.ranking_list.addButton(0, "button.png", data.config.WIDTH * 0.1 - (button_width) / 2 , data.config.HEIGHT * 0.1 - (button_height) / 2)

    def displayOutput(self, display):
        self.ranking_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.ranking_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                return screen.Menu()

        return self

    def update(self):
        pass

