import graphics
import gameplay

class HalfMoon(object):

    def __init__(self, pos, direction):

        self.animation = graphics.AnimationInfo()
        self.animation.alpha = lambda: 255 - (self.animation.timer - 8) * 32

        self.sprite = graphics.Sprite(63, "boss.png", pos)

        self.xVel = 5 * direction
        self.yVel = 0

        self.sprite.xScale = direction

        self.dead = False

    def draw(self, display, offset=(0, 0)):
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def getHurt(self, origin):
        pass

    def damage(self):
        return 2

    def update(self):
        self.animation.timer += 1

        self.sprite.x += self.xVel
        self.sprite.y += self.yVel

        if self.animation.timer >= 16:
            self.dead = True

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
            if entity.invincibility <= 0:
                if self.sprite.collidesWith(entity.sprite):
                    self.sprite.x -= 1000 * self.sprite.xScale
                    entity.getHurt(self)
                    self.sprite.x += 1000 * self.sprite.xScale
