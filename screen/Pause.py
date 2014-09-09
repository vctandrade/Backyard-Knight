import screen
import graphics
import pygame
import data

class Pause(object):

    def __init__(self):

        self.menu_list = graphics.userInterface.Interface()

        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3)
        self.menu_list.addButton(1, "button.png", data.config.WIDTH * 0.3, data.config.HEIGHT * 0.5)
        self.menu_list.addButton(2, "button.png", data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5)
        self.menu_list.addButton(3, "button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7)

        self.shadow = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
        self.shadow.set_alpha(224, pygame.RLEACCEL)

    def displayOutput(self, display):
        display.blit(self.shadow, (0, 0))
        self.menu_list.draw(display)

        graphics.drawText(display, data.translate("return"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.3, size=20 , formatting="center")
        graphics.drawText(display, data.translate("help"), data.config.WIDTH * 0.3, data.config.HEIGHT * 0.5, size=20 , formatting="center")
        graphics.drawText(display, data.translate("configurations"), data.config.WIDTH * 0.7, data.config.HEIGHT * 0.5, size=20 , formatting="center")
        graphics.drawText(display, data.translate("exit"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.7, size=20 , formatting="center")
        graphics.drawText(display, data.translate("pause"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.5, size=40 , color=0xFFFFFF, formatting="center")

    def respondToUserInput(self, event):
        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if e.button == 0:
                    return None
                if e.button == 1:
                    return screen.Help(screen.Pause)
                if e.button == 2:
                    return screen.ConfigMenu(screen.Pause)
                if e.button == 3:

                    pygame.mixer.music.fadeout(1024)

                    transitionTimer = 0
                    display = pygame.display.get_surface()
                    static = display.copy()

                    clock = pygame.time.Clock()

                    blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
                    blackness.fill(0x000000)

                    while transitionTimer <= 255:
                        display.blit(static, (0, 0))

                        blackness.set_alpha(transitionTimer, pygame.RLEACCEL)
                        display.blit(blackness, (0, 0))

                        transitionTimer += 4
                        pygame.display.flip()

                        clock.tick(60)

                    return screen.Menu(fadin=True)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return None

        return self

    def update(self):
        pass
