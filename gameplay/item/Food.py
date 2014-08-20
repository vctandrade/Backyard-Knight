import random
import data

class Food(object):

    def __init__(self):
        self.icon_index = random.randint(0, 7)
        self.icon = data.getResource("items.png")[self.icon_index]

    def use(self, player):
        if player.health != player.maxHealth:
            player.health += 1
            player.item = None
