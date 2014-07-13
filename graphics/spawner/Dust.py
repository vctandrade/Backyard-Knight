import graphics
import random
import math
import data

class Dust(object):
    
    def __init__(self):
        self.handler = graphics.SpriteHandler(0, "sprite2.png")
    
    def spawn(self):
        randPos = random.randint(0, data.config.WIDTH), random.randint(0, data.config.HEIGHT)
        randVel = random.random()*2 - 1, random.random()*2 - 1
        
        info = graphics.AnimationInfo()
        
        info.set(
                 x = lambda: randPos[0] + randVel[0]*info.timer,
                 y = lambda: randPos[1] + randVel[1]*info.timer,
                 
                 xScale = lambda: math.sin(info.timer*math.pi/100)*0.5,
                 yScale = lambda: math.sin(info.timer*math.pi/100)*0.5,
                 
                 alpha = lambda: math.sin(info.timer*math.pi/100)*255,
                 
                 deathTime = 100
                 )
        
        self.handler.spawn(randPos, alpha=0, scale=(0,0), info=info)
    
    def draw(self, display):
        self.handler.draw(display)
    
    def update(self):
        self.handler.update()