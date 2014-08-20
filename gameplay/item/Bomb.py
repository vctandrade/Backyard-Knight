import gameplay
import data

class Bomb(object):

    def __init__(self):
        self.icon = data.getResource("items.png")[13]

    def use(self, player):
        pos = (player.sprite.x, player.sprite.y)

        newBomb = gameplay.entity.Bomb(player.world, pos)
        newBomb.xVel = player.sprite.xScale * 4
        newBomb.yVel = -6

        if player.stance == "crouched":
            newBomb.sprite.y += 18
            newBomb.xVel *= 1.8
            newBomb.yVel = 0

        player.world.entities.append(newBomb)
        player.item = None
