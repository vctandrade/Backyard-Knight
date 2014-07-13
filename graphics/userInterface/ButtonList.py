from Button import Button
import pygame

class ButtonList(object):
    
    def __init__(self):
        self.buttons = list()
    
    def __getitem__(self, i):
        return self.buttons[i]
    
    def add(self, index, iconPath, x, y, active=True, visible=True, mask=None):
        self.buttons.append(Button(index, iconPath, x, y, active, visible, mask))
        self.buttons[-1].updateHover(pygame.mouse.get_pos())
    
    def handle(self, event):
        indexList = list()
        
        if event.type == pygame.MOUSEMOTION:
            for b in self.buttons:
                b.updateHover(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for b in self.buttons:
                b.clickDown()
        
        if event.type == pygame.MOUSEBUTTONUP:
            for b in self.buttons:
                if b.clickUp(): indexList.append(b.index)
        
        return indexList
    
    def draw(self, display):
        for b in self.buttons:
            display.blit(b.getIcon(), b.getDrawPos())