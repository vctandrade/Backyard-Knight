
class AnimationInfo():
    def __init__(self):
        self.timer = 0
        self.deathTime = -1

    def set(self, **value):
        for key in value:
            self.__dict__[key] = value[key]

    def animate(self, target):
        for attr in self.__dict__:
            if attr in target.__dict__:
                target.__setattr__(attr, self.__dict__[attr]())
