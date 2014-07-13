import pygame

class KeyHandler(object):
    
    def __init__(self):
        self.keyState = dict()
    
    def listenTo(self, *key):
        self.keyState.clear()
        for k in key:
            self.keyState[k] = False
    
    def handle(self, event):            
        if event.type == pygame.KEYDOWN:
            if event.key in self.keyState:
                self.keyState[event.key] = True
            
        if event.type == pygame.KEYUP:
            if event.key in self.keyState:
                self.keyState[event.key] = False
    
    def __getitem__(self, i):
        return self.keyState[i]