
BUTTONCLICKED = 33
HOVER = 34

NOHOVER = 0
CLICKHOVER = 1
TEXTHOVER = 2

class ButtonClicked:
    type = BUTTONCLICKED

    def __init__(self, button):
        self.button = button

class Hover:
    type = HOVER

    def __init__(self, mode):
        self.mode = mode
