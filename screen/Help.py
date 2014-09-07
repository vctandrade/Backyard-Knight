import graphics
import pygame
import screen
import data

class Help(object):

    def __init__(self, origin):
        self.origin = origin

        self.help_list = graphics.userInterface.Interface()
        self.help_images = ["key.png", "item.png"]
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

            if self.help_images[self.image] == "key.png":
                graphics.drawText(display, data.translate("pause"), data.config.WIDTH * 0.25, data.config.HEIGHT * 0.63, size=30)
                graphics.drawText(display, data.translate("jump"), data.config.WIDTH * 0.25, data.config.HEIGHT * 0.76, size=30)
                graphics.drawText(display, data.translate("attack"), data.config.WIDTH * 0.45, data.config.HEIGHT * 0.63, size=30)
                graphics.drawText(display, data.translate("use item"), data.config.WIDTH * 0.45, data.config.HEIGHT * 0.76, size=24)
                graphics.drawText(display, data.translate("open"), data.config.WIDTH * 0.65, data.config.HEIGHT * 0.63, size=30)
                graphics.drawText(display, data.translate("move"), data.config.WIDTH * 0.65, data.config.HEIGHT * 0.76, size=30)
            if self.help_images[self.image] == "item.png":
                graphics.drawText(display, data.translate("chest1"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.45, size=20)
                graphics.drawText(display, data.translate("chest2"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.5, size=20)
                graphics.drawText(display, data.translate("chest3"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.55, size=20)
                graphics.drawText(display, data.translate("chest4"), data.config.WIDTH * 0.02, data.config.HEIGHT * 0.6, size=12)
                graphics.drawText(display, data.translate("food"), data.config.WIDTH * 0.85, data.config.HEIGHT * 0.38, size=30)
                graphics.drawText(display, data.translate("potions"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5, size=30)
                graphics.drawText(display, data.translate("bomb"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.71, size=30)
                graphics.drawText(display, data.translate("weapons"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.6, size=30)


        display.blit(data.getResource(self.help_images[self.image]), (data.config.WIDTH * 0.2, data.config.HEIGHT * 0.15))
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
