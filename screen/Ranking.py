import graphics
import screen
import data

class Ranking(object):

    def __init__(self):
        self.ranking_list = graphics.userInterface.Interface()

        self.ranking_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1,mask="arrow_leftMask.png")

    def displayOutput(self, display):
        self.ranking_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.ranking_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                return screen.Menu()

        return self

    def update(self):
        pass

