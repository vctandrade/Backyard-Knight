import graphics

class Spear(object):

    def __init__(self):
        self.jump = 30

        self.pre = 15
        self.swing = 20
        self.pos = 10

        self.swing += self.pre
        self.pos += self.swing

        self.damage = 1

        self.xFix = [0, 34, 34, 0, 32, 32, 0, 28, 28]
        self.yFix = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.sprite = graphics.Sprite(0, "sword.png", (0, 0))
