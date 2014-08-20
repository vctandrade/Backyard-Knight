import data

class InvincibilityPotion(object):

    def __init__(self):
            self.icon = data.getResource("items.png")[10]

    def use(self, player):
        player.invincibility = 512
        player.item = None
