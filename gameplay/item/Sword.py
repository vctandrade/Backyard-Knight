import graphics

class Sword(object):

    def __init__(self):
        self.jump = 8

        self.pre = 12
        self.swing = 8
        self.pos = 16

        self.swing += self.pre
        self.pos += self.swing

        self.damage = 1

        self.xFix = [-30, 46, 46, -24, 44, 44, -28, 44, 44]
        self.yFix = [-16, -2, -2, 2, 12, 12, -20, 0, 0]

        self.firstIndex = 0

        self.sprite = graphics.Sprite(0, "hamword.png", (0, 0))
        self.icon = graphics.Sprite(16, "items.png", (0, 0))
