
class InvincibilityPotion(object):

    def use(self, player):
        player.invincibility = 512
        player.item = None
