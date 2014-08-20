import gameplay
import keyboard
import pygame
import data

class GamePlayTest(object):

    def __init__(self):
        self.world = gameplay.level.Test()
        keyboard.setMultiKeys(pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_x)

    def displayOutput(self, display):
        self.world.draw(display)

        for i in range(self.world.player.maxHealth / 2 + self.world.player.maxHealth % 2):
            if self.world.player.health >= 2 + 2 * i:
                display.blit(data.getResource("life.png")[0], (24 + i * 48, 32))
            if self.world.player.health == 1 + 2 * i:
                display.blit(data.getResource("life.png")[1], (24 + i * 48, 32))
            if self.world.player.health < 1 + 2 * i:
                display.blit(data.getResource("life.png")[2], (24 + i * 48, 32))

        display.blit(data.getResource("weapon_box.png"), (data.config.WIDTH - 152, 24))
        display.blit(data.getResource("item_box.png"), (data.config.WIDTH - 80, 24))

        if self.world.player.item != None:
            self.world.player.item.icon.draw(display, (50 - data.config.WIDTH, -54))
        self.world.player.weapon.icon.draw(display, (122 - data.config.WIDTH, -54))


    def respondToUserInput(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: self.world.player.moveRight()
            if event.key == pygame.K_LEFT: self.world.player.moveLeft()
            if event.key == pygame.K_DOWN: self.world.player.crouch()
            if event.key == pygame.K_z: self.world.player.jump()
            if event.key == pygame.K_x: self.world.player.attack()
            if event.key == pygame.K_c: self.world.player.useItem()

        return self

    def update(self):
        self.world.update()
