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
keyboard.setMultiKeys(pygame.K_a)
screen = screen.TextFieldTest()

def repaint():
    display.fill(0x000000)
    screen.displayOutput(display)
    pygame.display.flip()

def handleInput():
    global screen

    for event in pygame.event.get():
        if hasattr(event, "key"): keyboard.handle(event)
        elif event.type == pygame.QUIT: screen = None
        else: screen = screen.respondToUserInput(event)

    for event in keyboard.getPressed():
        screen = screen.respondToUserInput(event)

    keyboard.tick()

while screen is not None:
    repaint()
    screen.update()
    handleInput()

    clock.tick(60)

pygame.quit()
