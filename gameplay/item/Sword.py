import graphics

class Sword(object):

    def __init__(self):
        self.jump = 8

        self.pre = 8
        self.swing = 8
        self.pos = 16

        self.swing += self.pre
        self.pos += self.swing

        self.damage = 1

        self.xFix = [0, 42, 42, 0, 32, 32]

        self.sprite = graphics.Sprite(0, "sword.png", (0, 0))
