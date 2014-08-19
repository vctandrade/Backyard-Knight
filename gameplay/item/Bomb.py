import gameplay

class Bomb(object):

    def use(self, player):
        newBomb = gameplay.entity.Bomb(player.world, [player.sprite.x, player.sprite.y])
        newBomb.xVel = player.sprite.xScale * 5
        newBomb.yVel = -4

        player.world.entities.append(newBomb)
        player.item = None
