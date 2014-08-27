import graphics
import pygame
import screen
import data

class Help(object):

    def __init__(self, origin):
        self.origin = origin

        self.help_list = graphics.userInterface.Interface()
        self.help_images = ["help_image1.png", "help_image2.png", "help_image3.png"]
        self.image = 0

        self.help_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.help_list.addButton(1, "arrow_left.png", data.config.WIDTH * 0.4, data.config.HEIGHT * 0.9, mask="arrow_leftMask.png")
        self.help_list.addButton(2, "arrow_right.png", data.config.WIDTH * 0.6, data.config.HEIGHT * 0.9, mask="arrow_rightMask.png")

    def displayOutput(self, display):
        if not isinstance(self.origin, screen.Menu):
            resolution = (data.config.WIDTH, data.config.HEIGHT)
            shadow = pygame.Surface(resolution, pygame.SRCALPHA)
            shadow.fill((0, 0, 0, 128))
            display.blit(shadow, (0, 0))
        else: display.blit(data.getResource("rocks.png"), (0, 0))

        display.blit(data.getResource(self.help_images[self.image]), (400, 200))
        self.help_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.help_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    if e.button == 0:
                        return self.origin
                    if e.button == 1 :
                        self.image -= 1
                    if e.button == 2:
                        self.image += 1

                    self.image %= 3

        return self

    def update(self):
        pass
