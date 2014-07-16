import data
import graphics
import pygame
 
class TextField(object):
     
    def __init__(self, image, x, y, text="", focused=False, active=True, visible=True, mask=None):
         
        self.image = image
        self.mask = mask
         
        self.text = text
        self.pos = 0
         
        self.width = data.getResource(image).get_width()
        self.height = data.getResource(image).get_height()
         
        self.x = x
        self.y = y
        
        self.active = active
        self.visible = visible
        self.hovered = False
        self.clicked = False
        self.focused = focused
     
    def toggleActive(self):
        if self.active == True:
            self.active = False
        else: self.active = True
     
    def toggleVisible(self):
        if self.visible == True:
            self.visible = False
        else: self.visible = True
     
    def getIcon(self):
        if not self.visible: return graphics.blankImage
        return data.getResource(self.image)
     
    def getDrawPos(self):
        return [(self.x, self.y), (0, 0)]
     
    def updateHover(self, pos):
        x = pos[0] - self.x
        y = pos[1] - self.y
         
        mask = data.getResource(self.mask)
         
        if 0 <= x < self.width and 0 <= y < self.height \
        and (mask == None or mask[x][y] == 0xFF):
                self.hovered = True
             
        else:
            self.hovered = False
            self.clicked = False
     
    def clickDown(self):
        if self.hovered: self.clicked = True
         
    def clickUp(self):
        if self.clicked and self.hovered and self.active:
            self.clicked = False
            self.focused = True
            return
         
        self.focused = False
        self.clicked = False
        return
     
    def inputText(self, event):
        if event.type != pygame.KEYDOWN or not self.focused or not self.active:
            return
         
        if " " <= event.unicode <= "~":
            self.text = self.text[:self.pos] + event.unicode + self.text[self.pos:]
            self.pos += 1
         
        if event.key == pygame.K_BACKSPACE:
            if self.pos > 0: 
                self.text = self.text[:self.pos-1] + self.text[self.pos:]
                self.pos -= 1
        
        if event.key == pygame.K_DELETE:
            if self.pos < len(self.text):
                self.text = self.text[:self.pos] + self.text[self.pos+1:]
        
        if event.key == pygame.K_HOME:
            self.pos = 0
           
        if event.key == pygame.K_END:
            self.pos = len(self.text)
        
        if event.key == pygame.K_RIGHT:
            if self.pos < len(self.text):
                self.pos += 1
        
        if event.key == pygame.K_LEFT:
            if self.pos > 0: self.pos -= 1
        
        print self.text, self.pos
     
    def __setattr__(self, name, value):
        self.__dict__[name] = value
         
        if self.__dict__.has_key('clicked'):
            if name == 'x' or name == 'y':
                self.updateHover(pygame.mouse.get_pos())