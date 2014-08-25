import graphics
import gameplay
import math

class SettledSpike(object):

    def __init__(self, world, pos, mode):
        self.world = world
        self.mode = mode
        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "spike_change.png", pos)

        self.xVel, self.yVel = (0, 0)

        self.dead = False

        self.moveTimer = 0
        self.up = 1
        self.down = -1
        
        if self.mode == "UpDown":
            self.upLimit = self.sprite.y + self.sprite.height
            self.downLimit = self.sprite.y
        if self.mode == "DownUp":
            self.sprite.yScale = -1
            
            self.up = -1
            self.down = 1
            
            self.upLimit = self.sprite.y - self.sprite.height
            self.downLimit = self.sprite.y
        if self.mode == "LeftRight":
            self.sprite.angle = 90
            
            self.upLimit = self.sprite.x + self.sprite.height
            self.downLimit = self.sprite.x                 
        if self.mode == "RightLeft":  
            self.sprite.angle = 270        
            self.up = -1
            self.down = 1

            self.upLimit = self.sprite.x - self.sprite.height
            self.downLimit = self.sprite.x
            
    def draw(self, display, offset=(0, 0)):            
        self.animation.index = lambda: (self.animation.timer / 7) % 7
        
        self.animation.timer += 1
        self.animation.animate(self.sprite)
        self.sprite.draw(display, offset)

    def update(self):
        self.sprite.y += self.yVel
        self.sprite.x += self.xVel
        
        if self.mode == "UpDown":
            if self.sprite.y >= self.upLimit:
                self.yVel = 0
                self.moveDown()
            if self.sprite.y <= self.downLimit:
                self.moveUp()
                
        if self.mode == "DownUp":
            if self.sprite.y <= self.upLimit:
                self.yVel = 0
                self.moveDown()
            if self.sprite.y >= self.downLimit:
                self.moveUp()
                
        if self.mode == "RightLeft":
            if self.sprite.x <= self.upLimit:
                self.xVel = 0
                self.moveDown()
            if self.sprite.x >= self.downLimit:
                self.moveUp()
                
        if self.mode == "LeftRight":
            if self.sprite.x >= self.upLimit:
                self.xVel = 0
                self.moveDown()
            if self.sprite.x <= self.downLimit:
                self.moveUp()
        
    def moveUp(self):
        if self.mode == "DownUp" or self.mode == "UpDown":
            self.yVel = 20 * self.up
        else:
            self.xVel = 20 * self.up
            
    def moveDown(self):
        if self.mode == "DownUp" or self.mode == "UpDown":
            self.yVel = 2 * self.down
        else:
            self.xVel = 2 * self.down
    def getHurt(self, origin):
        self.world.player.knockBack(self)

    def collided(self):
        l = int(self.sprite.x - self.sprite.xCenter) / gameplay.tile.size
        r = int(self.sprite.x + self.sprite.xCenter - 1) / gameplay.tile.size

        t = int(self.sprite.y - self.sprite.yCenter + self.upperBox) / gameplay.tile.size
        b = int(self.sprite.y + self.sprite.yCenter - 1) / gameplay.tile.size

        for x in range(l, r + 1):
            for y in range(t, b + 1):
                if self.world.map[y][x].isColidable():
                    return True

        return False

    def damage(self):
        return 2

    def living(self):
        return True

    def GetHurt(self):
        pass

    def collidedWith(self, entity):
        if isinstance(entity, gameplay.entity.Player):
                entity.getHurt(self)
