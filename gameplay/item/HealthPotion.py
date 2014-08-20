import data

class HealthPotion(object):

    def __init__(self):
        self.icon = data.getResource("items.png")[9]

    def use(self, player):
        if player.health != player.maxHealth:
            player.health = player.maxHealth
            player.item = None
