import gameplay
import data

class World(object):

    def __init__(self):
        self.map = gameplay.level.Test()

        self.player = gameplay.entity.Player(self.map)
        self.player.sprite.x = 512
        self.player.sprite.y = 400

        self.camera = [0, 0]

    def draw(self, display):
        self.map.draw(display, offset=self.camera)
        self.player.draw(display, offset=self.camera)

    def update(self):
        self.player.update()
        self.map.update()
        self.updateCamera()
        pass

    def updateCamera(self):
        x = self.player.sprite.x - data.config.WIDTH / 2
        y = self.player.sprite.y - data.config.HEIGHT / 2

        if abs(self.camera[0] - x) > 8:
            self.camera[0] += (x - self.camera[0]) / 32

        if abs(self.camera[1] - y) > 8:
            self.camera[1] += (y - self.camera[1]) / 32

        return x, y
