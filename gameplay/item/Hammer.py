import graphics

class Hammer(object):

    def __init__(self):
        self.jump = 4

        self.pre = 20
        self.swing = 15
        self.pos = 10

        self.swing += self.pre
        self.pos += self.swing

        self.damage = 1.5

        self.xFix = [-30, 46, 46, -24, 44, 44, -28, 44, 44]
        self.yFix = [-16, -2, -2, 2, 12, 12, -20, 0, 0]

        self.firstIndex = 3

        self.sprite = graphics.Sprite(0, "hamword.png", (0, 0))
        self.icon = graphics.Sprite(18, "items.png", (0, 0))
