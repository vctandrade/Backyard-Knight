
class HealthPotion(object):

    def use(self, player):
        if player.health != player.maxHealth:
            player.health = player.maxHealth
            player.item = None
