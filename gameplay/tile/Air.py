import data

class Air(object):

    def getSprite(self):
        return data.getResource("tiles.png")[1]

    def isColidable(self):
        return False
