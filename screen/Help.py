import graphics
import pygame
import screen
import data

class Help(object):

    def __init__(self, origin):
        self.origin = origin

        self.help_list = graphics.userInterface.Interface()
        self.image = 0

        self.help_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.help_list.addButton(1, "arrow_left.png", data.config.WIDTH * 0.4, data.config.HEIGHT * 0.9, mask="arrow_leftMask.png")
        self.help_list.addButton(2, "arrow_right.png", data.config.WIDTH * 0.6, data.config.HEIGHT * 0.9, mask="arrow_rightMask.png")

    def displayOutput(self, display):
        if self.origin is not screen.Menu:
            resolution = (data.config.WIDTH, data.config.HEIGHT)
            shadow = pygame.Surface(resolution, pygame.SRCALPHA)
            shadow.fill((0, 0, 0, 224))
            display.blit(shadow, (0, 0))
        else:
            display.fill((0, 90, 150))

            if self.image % 2 == 0:

                display.blit(data.getResource("help_esc.png"), (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.25))
                display.blit(data.getResource("help_Z.png"), (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.35))
                display.blit(data.getResource("help_X.png"), (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.45))
                display.blit(data.getResource("help_C.png"), (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.55))

                display.blit(data.getResource("help_up.png"), (data.config.WIDTH * 0.5, data.config.HEIGHT * 0.25))
                display.blit(data.getResource("help_down.png"), (data.config.WIDTH * 0.5, data.config.HEIGHT * 0.35))
                display.blit(data.getResource("help_left.png"), (data.config.WIDTH * 0.5, data.config.HEIGHT * 0.45))
                display.blit(data.getResource("help_right.png"), (data.config.WIDTH * 0.55, data.config.HEIGHT * 0.45))

                graphics.drawText(display, data.translate("controls"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=40, formatting="center")

                graphics.drawText(display, data.translate("pause"), data.config.WIDTH * 0.2 + 100, data.config.HEIGHT * 0.27, size=20)
                graphics.drawText(display, data.translate("jump"), data.config.WIDTH * 0.2 + 100, data.config.HEIGHT * 0.38, size=20)
                graphics.drawText(display, data.translate("attack"), data.config.WIDTH * 0.2 + 100, data.config.HEIGHT * 0.47, size=20)
                graphics.drawText(display, data.translate("use item"), data.config.WIDTH * 0.2 + 100, data.config.HEIGHT * 0.58, size=20)

                graphics.drawText(display, data.translate("open"), data.config.WIDTH * 0.5 + 100, data.config.HEIGHT * 0.28, size=20)
                graphics.drawText(display, data.translate("crouch"), data.config.WIDTH * 0.5 + 100, data.config.HEIGHT * 0.38, size=20)
                graphics.drawText(display, data.translate("move"), data.config.WIDTH * 0.55 + 100, data.config.HEIGHT * 0.48, size=20)

                graphics.drawText(display, data.translate("jump higher"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.75, size=18, formatting="center")
            else:

                display.blit(data.getResource("items.png")[0], (data.config.WIDTH * 0.4, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[1], (data.config.WIDTH * 0.45, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[2], (data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[3], (data.config.WIDTH * 0.55, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[4], (data.config.WIDTH * 0.6, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[5], (data.config.WIDTH * 0.65, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[6], (data.config.WIDTH * 0.7, data.config.HEIGHT * 0.3))
                display.blit(data.getResource("items.png")[7], (data.config.WIDTH * 0.75, data.config.HEIGHT * 0.3))

                display.blit(data.getResource("items.png")[8], (data.config.WIDTH * 0.75, data.config.HEIGHT * 0.4))
                display.blit(data.getResource("items.png")[9], (data.config.WIDTH * 0.7, data.config.HEIGHT * 0.4))

                display.blit(data.getResource("items.png")[16], (data.config.WIDTH * 0.75, data.config.HEIGHT * 0.5))
                display.blit(data.getResource("items.png")[17], (data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5))
                display.blit(data.getResource("items.png")[18], (data.config.WIDTH * 0.65, data.config.HEIGHT * 0.5))

                display.blit(data.getResource("items.png")[11], (data.config.WIDTH * 0.75, data.config.HEIGHT * 0.6))
                display.blit(data.getResource("chest.png")[0], (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.3))

                graphics.drawText(display, data.translate("items"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=30, formatting="center")

                graphics.drawText(display, data.translate("chest1"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.45, size=20)
                graphics.drawText(display, data.translate("chest2"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.5, size=20)
                graphics.drawText(display, data.translate("chest3"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.55, size=20)
                graphics.drawText(display, data.translate("chest4"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.6, size=12)
                graphics.drawText(display, data.translate("food"), data.config.WIDTH * 0.88, data.config.HEIGHT * 0.33, size=20, formatting="center")
                graphics.drawText(display, data.translate("potions"), data.config.WIDTH * 0.88, data.config.HEIGHT * 0.43, size=20, formatting="center")
                graphics.drawText(display, data.translate("bomb"), data.config.WIDTH * 0.88, data.config.HEIGHT * 0.63, size=20, formatting="center")
                graphics.drawText(display, data.translate("weapons"), data.config.WIDTH * 0.88, data.config.HEIGHT * 0.53, size=20, formatting="center")


        self.help_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.help_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    if e.button == 0:
                        return self.origin()
                    if e.button == 1 :
                        self.image -= 1
                    if e.button == 2:
                        self.image += 1
                    self.image %= 2

        return self

    def update(self):
        pass
