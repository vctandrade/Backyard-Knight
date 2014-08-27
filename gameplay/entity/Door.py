import graphics
import gameplay
import pygame

class Door(object):

    def __init__(self, world, pos, nextLvl):
        self.world = world
        self.next = nextLvl

        self.sprite = graphics.Sprite(56, "golem.png", (0, 0))
        self.sprite.x, self.sprite.y = pos

        self.sprite.yCenter = 212

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.sprite.draw(display, offset)

    def use(self):
        self.world.static = pygame.display.get_surface().copy()
        self.world.next = self.next(self.world.player)

    def collidedWith(self, origin):
        if isinstance(origin, gameplay.entity.Player):
            origin.interactibles.add(self)

    def update(self):
        try: self.world.player.interactibles.remove(self)
        except: pass

    def living(self):
        return False
