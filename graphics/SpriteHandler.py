import graphics

class SpriteHandler(object):
    
    def __init__(self, index, spritePath):
        self.index = index
        self.table = spritePath
        
        self.spriteList = list()
        self.spriteInfo = list()
    
    def spawn(self, pos, alpha=255, angle=0, scale=(1,1), info=graphics.AnimationInfo()):
        newSprite = graphics.Sprite(self.index, self.table, pos)
        
        newSprite.alpha = alpha
        newSprite.angle = angle
        newSprite.xScale, newSprite.yScale = scale
        
        self.spriteList.append(newSprite)
        self.spriteInfo.append(info)
    
    def draw(self, display, offset=(0,0)):
        for sprite in self.spriteList:
            sprite.draw(display, offset)
    
    def remove(self, i):
        self.spriteList.pop(i)
        self.spriteInfo.pop(i)
    
    def update(self):
        i=0
        while i < len(self.spriteList):
            
            self.spriteInfo[i].animate(self.spriteList[i])
            
            self.spriteInfo[i].timer += 1
            if self.spriteInfo[i].timer == self.spriteInfo[i].deathTime:
                self.remove(i)
            
            i+=1