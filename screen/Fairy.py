import graphics
import pygame
import screen

class Fairy(object):
    
    def __init__(self):
        self.fairyDustSpawner = graphics.spawner.FairyDust()
        graphics.userInterface.cursor.setFairy()
        self.timer = 0
        
        pass
    
    def displayOutput(self, display):
        self.fairyDustSpawner.draw(display)
        graphics.userInterface.cursor.draw(display)
        
        pass
    
    def respondToUserInput(self, event):              
        if event.type == pygame.MOUSEMOTION:                            
            self.fairyDustSpawner.spawn(event.pos)
        
        if event.type == pygame.MOUSEBUTTONUP:
            return screen.Main()
            
        return self
    
    def update(self):
        
        self.fairyDustSpawner.update()
        graphics.userInterface.Cursor().update()
        
        self.timer+=1
        if self.timer%10==0:
            self.fairyDustSpawner.spawn(pygame.mouse.get_pos())
        
        pass
    