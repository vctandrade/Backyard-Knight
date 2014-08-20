import gameplay

class Bomb(object):

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
