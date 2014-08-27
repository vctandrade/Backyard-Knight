import graphics
import screen
import data

class Credits(object):

    def __init__(self):
        self.credits_list = graphics.userInterface.Interface()

        self.credits_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1,mask = "arrow_leftMask.png")
        self.credits_list.addButton(1,"button.png", data.config.WIDTH * 0.05, data.config.HEIGHT * 0.5)
    def displayOutput(self, display):
        display.blit(data.getResource("credits.png"), (0, 0))
        self.credits_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.credits_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    if e.button == 1: return screen.ConfigMenu(self)
                    else: return screen.Menu()
        return self

    def update(self):
        pass
