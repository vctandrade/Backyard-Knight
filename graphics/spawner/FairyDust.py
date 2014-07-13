import graphics
import random

class FairyDust(object):
    
    def __init__(self):
        self.handler = graphics.SpriteHandler(2, "sprite.png")
    
    def spawn(self, pos):        
        randVel = random.random()*2-1, random.random()*2-1
        spriteInfo = graphics.AnimationInfo()
        
        spriteInfo.set(
                       x = lambda: pos[0] + randVel[0]*spriteInfo.timer,
                       y = lambda: pos[1] + randVel[1]*spriteInfo.timer,
                       
                       alpha = lambda: 255 - 5*spriteInfo.timer,
                       deathTime = 50
                       )
            
        self.handler.spawn(pos, info=spriteInfo)
    
    def draw(self, display):
        self.handler.draw(display)
    
    def update(self):
        self.handler.update()