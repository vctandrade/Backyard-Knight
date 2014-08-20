import random
import graphics

class Food(object):

    def __init__(self):
        self.icon = graphics.Sprite(random.randint(0, 7), "items.png", (0, 0))

    def use(self, player):
        if player.health != player.maxHealth:
            player.health += 1
            player.item = None
