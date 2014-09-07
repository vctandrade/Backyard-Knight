import graphics

class Spear(object):

    def __init__(self):
        self.jump = 24

        self.pre = 16
        self.swing = 18
        self.pos = 12

        self.swing += self.pre
        self.pos += self.swing

        self.damage = 1

        self.xFix = [-8, 22, 22, -8, 16, 16, -6, 20, 20]
        self.yFix = [18, 16, 16, 28, 26, 26, 16, 14, 14]

        self.firstIndex = 0

        self.sprite = graphics.Sprite(0, "spear.png", (0, 0))
        self.icon = graphics.Sprite(17, "items.png", (0, 0))
