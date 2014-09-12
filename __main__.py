import pygame
import screen
import keyboard
import graphics
import data

pygame.mixer.pre_init(buffer=1024)
pygame.init()

pygame.mixer.set_num_channels(16)

data.loadConfig()
data.loadLanguage()

pygame.display.set_icon(pygame.image.load("icon.png"))
pygame.display.set_caption(data.translate("caption"))
resolution = data.config.WIDTH, data.config.HEIGHT

if data.config.FULLSCREEN:
    display = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
else: display = pygame.display.set_mode(resolution)

data.loadResources()
graphics.userInterface.cursor.init()

clock = pygame.time.Clock()
screen = screen.Introduction()

def repaint():
    display.fill(0x000000)
    screen.displayOutput(display)
    graphics.userInterface.cursor.draw(display)
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
    graphics.userInterface.cursor.update()

while screen is not None:
    repaint()
    screen.update()
    handleInput()

    clock.tick(60)

pygame.quit()
