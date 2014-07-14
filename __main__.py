import pygame
import screen
import keyboard
import data

pygame.init()

data.loadConfig()
data.loadResources()

data.loadLanguage(data.config.LANG)

pygame.display.set_caption(data.translate("caption"))
resolution = data.config.WIDTH, data.config.HEIGHT
display = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

screen = screen.Main()

def repaint():
    display.fill(0x000000)
    screen.displayOutput(display)
    pygame.display.flip()

def handleInput():
    global screen
    
    screen.respondToUserInput(keyboard.Event)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen = None
        else: screen = screen.respondToUserInput(event)

while screen is not None:
    screen.update()
    repaint()
    handleInput()
    
    clock.tick(60)
        
pygame.quit()
