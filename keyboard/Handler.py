import pygame
import keyboard

delay = 20
period = 4

ticks = 0
lastUni = None
    
def handle(event):
    global lastUni, ticks
             
    if event.type == pygame.KEYDOWN:
        lastUni = event
        ticks = 0
        
    if event.type == pygame.KEYUP:
        lastUni = None
        ticks = 0

def tick():
    global ticks
    if lastUni: ticks += 1

def getPressed():
    eventList = list()
    
    if (lastUni == None or ticks > 1) and (ticks < delay or ticks % period > 0): pass
    else: eventList.append(lastUni)
    
    return pygame.event.Event(keyboard.PRESSED, keys=eventList)