import gameplay
import keyboard
import pygame

class GamePlayTest(object):

    def __init__(self):
        keyboard.setMultiKeys(pygame.K_a, pygame.K_d, pygame.K_s)
        self.world = gameplay.World()

    def displayOutput(self, display):
        self.world.draw(display)

    def respondToUserInput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: self.world.player.moveRight()
            if event.key == pygame.K_a: self.world.player.moveLeft()
            if event.key == pygame.K_s: self.world.player.crouch()
            if event.key == pygame.K_SPACE: self.world.player.jump()

        return self

    def update(self):
        self.world.update()
