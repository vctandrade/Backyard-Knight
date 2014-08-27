import data

class Dirt(object):

    def getSprite(self):
        return data.getResource("tiles.png")[0]

    def isColidable(self):
        return True
