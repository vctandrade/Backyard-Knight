import graphics
import pygame
import screen
import data

class Introduction(object):

    def __init__(self):
        data.playMusic("fade-to-black.ogg")
        self.transitionTimer = 0

    def displayOutput(self, display):
        textColor = 0xF0F0F0

        buf = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
        if self.transitionTimer < 1080:
            buf.set_alpha(5 * abs((self.transitionTimer + 180) % 360 - 180), pygame.RLEACCEL)

        if self.transitionTimer < 360:
            buf.blit(data.getResource("bob.png")[28], (data.config.WIDTH * 0.4 - 48, data.config.HEIGHT * 0.6 - 48))
            buf.blit(data.getResource("dog.png")[3], (data.config.WIDTH * 0.6 - 26, data.config.HEIGHT * 0.6 - 24))
            graphics.drawText(buf, data.translate("intro1"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4, color=textColor, size=20, formatting="center")
            graphics.drawText(buf, data.translate("intro2"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4 + 50, color=textColor, size=20, formatting="center")

        elif self.transitionTimer < 720:
            buf.blit(data.getResource("bob.png")[24], (data.config.WIDTH * 0.4 - 48, data.config.HEIGHT * 0.7 - 48))
            buf.blit(data.getResource("cage.png")[0], (data.config.WIDTH * 0.6 + 37, data.config.HEIGHT * 0.7 - 6))
            buf.blit(data.getResource("neighbour.png")[1], (data.config.WIDTH * 0.6 - 40, data.config.HEIGHT * 0.7 - 92))
            graphics.drawText(buf, data.translate("intro3"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4, color=textColor, size=20, formatting="center")
            graphics.drawText(buf, data.translate("intro4"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4 + 50, color=textColor, size=20, formatting="center")
            graphics.drawText(buf, data.translate("intro5"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4 + 100, color=textColor, size=20, formatting="center")

        elif self.transitionTimer < 1080:
            buf.blit(data.getResource("bob.png")[0], (data.config.WIDTH * 0.5 - 48, data.config.HEIGHT * 0.45 - 48))
            graphics.drawText(buf, data.translate("intro6"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.6, color=textColor, size=20, formatting="center")

        elif ((self.transitionTimer - 1002) / 16) % 4:
            graphics.drawText(buf, data.translate("press"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.5, color=textColor, size=20, formatting="center")

        display.blit(buf, (0, 0))

    def respondToUserInput(self, event):
            if event.type == pygame.KEYDOWN:

                pygame.mixer.music.fadeout(1024)

                transitionTimer = 0
                display = pygame.display.get_surface()

                clock = pygame.time.Clock()

                blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
                blackness.fill(0x000000)

                while transitionTimer <= 255:
                    self.displayOutput(display)

                    blackness.set_alpha(transitionTimer, pygame.RLEACCEL)
                    display.blit(blackness, (0, 0))

                    transitionTimer += 4
                    pygame.display.flip()

                    clock.tick(60)

                return screen.Menu(fadin=True)

            return self

    def update(self):
            self.transitionTimer += 1



