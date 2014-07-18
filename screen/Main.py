import pygame
import screen
import graphics

class Main(object):

    def __init__(self):
        graphics.userInterface.cursor.setDefault()
        self.dustSpawner = graphics.spawner.Dust()

        pass

    def displayOutput(self, display):
        self.dustSpawner.draw(display)

        pass

    def respondToUserInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            return screen.Fairy()

        return self

    def update(self):
        self.dustSpawner.update()
        self.dustSpawner.spawn()

        pass
