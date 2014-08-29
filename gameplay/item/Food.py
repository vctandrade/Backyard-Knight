import random
import graphics

class Food(object):

    def __init__(self):
        self.icon = graphics.Sprite(random.randint(0, 7), "items.png", (0, 0))

    def use(self, player):
        player.health = min(player.health + 1, player.maxHealth)
        player.item = None
