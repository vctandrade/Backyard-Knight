import gameplay
import graphics
import random
import data

class Food(object):

    def __init__(self):
        self.icon = graphics.Sprite(random.randint(0, 7), "items.png", (0, 0))

    def use(self, player):
        data.playSound("item.ogg")
        player.health = min(player.health + 1, player.maxHealth)
        player.item = None

        for i in range(8): player.world.particles.append(gameplay.entity.Sparkle(player.world, (player.sprite.x, player.sprite.y)))
