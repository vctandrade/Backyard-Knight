import graphics
import pygame
import screen
import data

class Win(object):

    def __init__(self, score):
        self.buttons = graphics.userInterface.Interface()
        self.buttons.addButton(0, "button.png", data.config.WIDTH * 0.35, data.config.HEIGHT * 0.4)
        self.buttons.addButton(1, "button.png", data.config.WIDTH * 0.65, data.config.HEIGHT * 0.4)

        self.score = score
        self.transitionTimer = 0

    def displayOutput(self, display):

        if self.transitionTimer >= 128:
            self.buttons.draw(display)

            graphics.drawText(display, data.translate("submit"), data.config.WIDTH * 0.35, data.config.HEIGHT * 0.4 - 15, size=20, formatting="center")
            graphics.drawText(display, data.translate("score"), data.config.WIDTH * 0.35, data.config.HEIGHT * 0.4 + 15, size=20, formatting="center")
            graphics.drawText(display, data.translate("exit"), data.config.WIDTH * 0.65, data.config.HEIGHT * 0.4, size=20, formatting="center")

        else:
            buf = pygame.Surface((200 + data.config.WIDTH * 0.3, 100), pygame.SRCALPHA)

            self.buttons.draw(buf, (data.config.WIDTH * 0.35 - 100, data.config.HEIGHT * 0.4 - 50))

            graphics.drawText(buf, data.translate("submit"), 100, 50 - 15, size=20, formatting="center")
            graphics.drawText(buf, data.translate("score"), 100, 50 + 15, size=20, formatting="center")
            graphics.drawText(buf, data.translate("exit"), 100 + data.config.WIDTH * 0.3, 50, size=20, formatting="center")

            buf.fill((255, 255, 255, self.transitionTimer * 2), special_flags=pygame.BLEND_RGBA_MULT)
            display.blit(buf, (data.config.WIDTH * 0.35 - 100, data.config.HEIGHT * 0.4 - 50))
            self.transitionTimer += 2

    def respondToUserInput(self, event):
        for e in self.buttons.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:

                if e.button == 0:
                    return screen.SubmitScore(self.score)

                if e.button == 1:

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

                    return screen.Credits(fadin=True)

        return self

    def update(self):
        pass
