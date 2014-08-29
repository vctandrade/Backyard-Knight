import graphics
import gameplay

class Door(object):

    def __init__(self, world, pos, nextLvl):
        self.world = world
        self.next = nextLvl

        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(56, "golem.png", (0, 0))
        self.sprite.x, self.sprite.y = pos

        self.sprite.yCenter = 212

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        if self.world.next:
            self.animation.index = lambda: 57 + (self.animation.timer / 24) % 3

        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)
        self.animation.timer += 1

    def use(self):
        self.world.next = self.next
        self.animation.timer = 0

    def getHurt(self, origin):
        pass

    def collidedWith(self, origin):
        if isinstance(origin, gameplay.entity.Player):
            origin.interactibles.add(self)

    def update(self):
        try: self.world.player.interactibles.remove(self)
        except: pass
