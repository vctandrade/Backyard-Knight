import graphics
import data

class InvincibilityPotion(object):

    def __init__(self):
            self.icon = graphics.Sprite(9, "items.png", (0, 0))

    def use(self, player):
        data.playSound("item.ogg")
        player.invincibility = 512
        player.item = None
