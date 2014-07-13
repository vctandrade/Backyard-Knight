import graphics
import pygame

class Cursor(object):
    
    sprite = None
    info = graphics.AnimationInfo()
    
    def setNone(self):
        pygame.mouse.set_visible(True)
        Cursor.sprite = None
       
    def setFairy(self):
        pygame.mouse.set_visible(False)
        Cursor.sprite = graphics.Sprite(3, "sprite.png", pygame.mouse.get_pos())
        Cursor.sprite.xScale, Cursor.sprite.yScale = 2, 2
        
        Cursor.info.clear()
        Cursor.info.set(index = lambda: 3 + (Cursor.info.timer % 6) / 3)
    
    def draw(self, display):
        if Cursor.sprite == None: return
        Cursor.sprite.draw(display)
    
    def update(self):
        if Cursor.sprite == None: return
            
        Cursor.info.timer += 1
        Cursor.info.animate(Cursor.sprite)
        Cursor.sprite.x, Cursor.sprite.y = pygame.mouse.get_pos()

cursor = Cursor()