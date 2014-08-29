import graphics
import gameplay
import random

class Chest(object):

    def __init__(self, world, pos):
        self.world = world

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "chest.png", (0, 0))

        self.sprite.x, self.sprite.y = pos
        self.state = "closed"

        self.dead = False

    def draw(self, display, offset=(0, 0)):

        if self.state == "closed":
            self.animation.index = lambda: 0
        if self.state == "open":
            self.animation.index = lambda: 1 + (self.animation.timer / 8) % 3 if self.animation.timer < 24 else 4

        self.animation.animate(self.sprite)

        self.sprite.draw(display, offset)

    def randomizeItem(self):
        chance = random.random()

        if chance < 0.14: item = gameplay.item.Sword()
        elif chance < 0.28: item = gameplay.item.Spear()
        elif chance < 0.42: item = gameplay.item.Hammer()
        elif chance < 0.56: item = gameplay.item.HealthPotion()
        elif chance < 0.60: item = gameplay.item.InvincibilityPotion()
        elif chance < 0.74: item = gameplay.item.Bomb()
        else: item = gameplay.item.Food()

        if type(item) in (type(self.world.player.item), type(self.world.player.weapon)):
            return self.randomizeItem()

        return item

    def use(self):
        if self.state == "closed":
            item = self.randomizeItem()

            if hasattr(item, "damage"):
                self.world.player.weapon = item
                self.world.player.flashMode = "weapon"

            else:
                self.world.player.item = item
                self.world.player.flashMode = "item"

            self.world.player.flashTimer = 32

            self.state = "open"
            self.animation.timer = 0

    def getHurt(self, origin):
        pass

    def collidedWith(self, origin):
        if isinstance(origin, gameplay.entity.Player):
            origin.interactibles.add(self)

    def update(self):
        self.animation.timer += 1
        try: self.world.player.interactibles.remove(self)
        except: pass

