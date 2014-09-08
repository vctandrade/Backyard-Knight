
import graphics
import screen
import data

class Credits(object):

    def __init__(self):
        self.credits_list = graphics.userInterface.Interface()

        self.credits_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")

    def displayOutput(self, display):
        display.fill((34, 177, 76))
        display.blit(data.getResource("credits_player.png"), (data.config.WIDTH * 0.18 - 160, data.config.HEIGHT * 0.55 - 264))
        display.blit(data.getResource("credits_dog.png"), (data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6))

        graphics.drawText(display, data.translate("credits"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=50, formatting="center")

        graphics.drawText(display, data.translate("students"), data.config.WIDTH * 0.6 - 300, data.config.HEIGHT * 0.25, size=30)
        graphics.drawText(display, "Victor Andrade", data.config.WIDTH * 0.60, data.config.HEIGHT * 0.25, size=20)
        graphics.drawText(display, "Marianne Linhares", data.config.WIDTH * 0.60, data.config.HEIGHT * 0.29, size=20)

        graphics.drawText(display, data.translate("professors"), data.config.WIDTH * 0.6 - 300, data.config.HEIGHT * 0.39, size=30)
        graphics.drawText(display, "Dalton Serey", data.config.WIDTH * 0.60 + 50, data.config.HEIGHT * 0.39, size=20)
        graphics.drawText(display, "Jorge Figueiredo", data.config.WIDTH * 0.60 + 50, data.config.HEIGHT * 0.43, size=20)

        graphics.drawText(display, data.translate("monitor"), data.config.WIDTH * 0.6 - 300 , data.config.HEIGHT * 0.53, size=30)
        graphics.drawText(display, "Klaudio Medeiros", data.config.WIDTH * 0.6 - 20, data.config.HEIGHT * 0.53, size=20)

        self.credits_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.credits_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    return screen.Menu()
        return self

    def update(self):
        pass
