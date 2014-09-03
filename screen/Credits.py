import graphics
import screen
import data

class Credits(object):

    def __init__(self):
        self.credits_list = graphics.userInterface.Interface()

        self.credits_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")

    def displayOutput(self, display):
        display.fill((34,177,76))
        display.blit(data.getResource("credits.png"),(data.config.HEIGHT * 0.1,data.config.HEIGHT * 0.1))
        
        graphics.drawText(display, data.translate("credits"),data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1,size=50, formatting ="center")
        graphics.drawText(display, data.translate("students"),data.config.WIDTH * 0.5, data.config.HEIGHT * 0.31,size=30, formatting ="center")
        graphics.drawText(display, data.translate("professors"),data.config.WIDTH * 0.5, data.config.HEIGHT * 0.42,size=30, formatting ="center")
        graphics.drawText(display, data.translate("monitor"),data.config.WIDTH * 0.5, data.config.HEIGHT * 0.545,size=30, formatting ="center")
        self.credits_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.credits_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    return screen.Menu()
        return self

    def update(self):
        pass
