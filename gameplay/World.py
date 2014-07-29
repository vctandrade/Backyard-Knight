import gameplay
import data

class World(object):

    def __init__(self):
        self.player = gameplay.entity.Player(self)
        self.player.sprite.x = 512
        self.player.sprite.y = 100

        self.map = gameplay.level.Test()

        self.camera = [0, 0]

    def draw(self, display):
        self.map.draw(display, offset=self.camera)
        self.player.draw(display, offset=self.camera)

    def update(self):
        self.player.update()
        self.updateCamera()
        pass

    def updateCamera(self):
        x = self.player.sprite.x - data.config.WIDTH / 2
        y = self.player.sprite.y - data.config.HEIGHT / 2

        if abs(self.camera[0] - x) > 1:
            self.camera[0] += (x - self.camera[0]) / 20

        if abs(self.camera[1] - y) > 1:
            self.camera[1] += (y - self.camera[1]) / 20

        return x, y
