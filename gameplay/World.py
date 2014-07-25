import gameplay
import data

class World(object):

    def __init__(self):
        self.player = gameplay.entity.Player(self)
        self.player.sprite.x = 512
        self.player.sprite.y = 200

        self.map = gameplay.level.Test()

    def draw(self, display):

        self.map.draw(display, offset=self.camera)
        self.player.draw(display, offset=self.camera)

    def update(self):
        self.player.update()
        pass

    @property
    def camera(self):
        x = self.player.sprite.x - data.config.WIDTH / 2
        y = self.player.sprite.y - data.config.HEIGHT / 2
        return x, y
