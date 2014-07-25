import gameplay
import keyboard
import pygame

class GamePlayTest(object):

    def __init__(self):
        keyboard.setMultiKeys(pygame.K_a, pygame.K_d)
        self.world = gameplay.World()

    def displayOutput(self, display):
        self.world.draw(display)

    def respondToUserInput(self, event):
        self.world.player.handle(event)

        return self

    def update(self):
        self.world.update()
