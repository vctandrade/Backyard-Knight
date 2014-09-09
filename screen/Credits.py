# coding: cp437

import graphics
import screen
import data

class Credits (object):

    def __init__(self):
        self.credits_list = graphics.userInterface.Interface()
        self.credits_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")

    def displayOutput(self, display):
        display.fill((34, 177, 76))
        display.blit(data.getResource("credits_player.png"), (data.config.WIDTH * 0.4 - 380, data.config.HEIGHT * 0.55 - 264))
        display.blit(data.getResource("credits_dog.png"), (data.config.WIDTH * 0.7 - 200, data.config.HEIGHT * 0.6))

        graphics.drawText(display, data.translate("credits"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=50, formatting="center")

        graphics.drawText(display, data.translate("students"), data.config.WIDTH * 0.7 - 400, data.config.HEIGHT * 0.25, size=30)
        graphics.drawText(display, "Victor Andrade", data.config.WIDTH * 0.7 - 100, data.config.HEIGHT * 0.25, size=20)

        graphics.drawText(display, "Marianne Linhares", data.config.WIDTH * 0.7 - 100, data.config.HEIGHT * 0.29, size=20)

        graphics.drawText(display, data.translate("professors"), data.config.WIDTH * 0.7 - 400, data.config.HEIGHT * 0.36 + 20, size=30)
        graphics.drawText(display, "Dalton Serey", data.config.WIDTH * 0.7 - 25, data.config.HEIGHT * 0.36 + 20, size=20)
        graphics.drawText(display, "Jorge Figueiredo", data.config.WIDTH * 0.7 - 25, data.config.HEIGHT * 0.40 + 20, size=20)

        graphics.drawText(display, data.translate("monitor"), data.config.WIDTH * 0.7 - 400 , data.config.HEIGHT * 0.47 + 40, size=30)
        graphics.drawText(display, "Kl udio Medeiros".decode("cp437"), data.config.WIDTH * 0.7 - 120, data.config.HEIGHT * 0.47 + 40, size=20)

        self.credits_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.credits_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    return screen.Menu()
        return self

    def update(self):
        pass
