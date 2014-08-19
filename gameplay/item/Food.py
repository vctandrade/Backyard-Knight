
class Food(object):

    def use(self, player):
        if player.health != player.maxHealth:
            player.health += 1
            player.item = None
