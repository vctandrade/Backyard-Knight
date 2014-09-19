import graphics
import keyboard
import screen
import pygame
import data

from operator import itemgetter

class SubmitScore (object):

    def __init__(self, score, dead=False):
        keyboard.setMultiKeys()

        self.menu_list = graphics.userInterface.Interface()
        self.menu_list.addButton(0, "button.png", data.config.WIDTH * 0.5 + 225, data.config.HEIGHT * 0.55, active=False)
        self.menu_list.addTextField("name", "textField.png", data.config.WIDTH * 0.5 - 125, data.config.HEIGHT * 0.55, color=0x000000, size=20, focused=True)

        self.winButtons = graphics.userInterface.Interface()
        self.winButtons.addButton(0, "button.png", data.config.WIDTH * 0.35, data.config.HEIGHT * 0.4)
        self.winButtons.addButton(1, "button.png", data.config.WIDTH * 0.65, data.config.HEIGHT * 0.4)

        self.color = 0xE0E0E0 if dead else 0x262626
        self.transitionTimer = 0 if not dead else 128
        self.score = score

    def displayOutput(self, display, offset=(0, 0)):

        if self.transitionTimer < 128:
            buf = pygame.Surface((200 + data.config.WIDTH * 0.3, 100), pygame.SRCALPHA)

            self.winButtons.draw(buf, (data.config.WIDTH * 0.35 - 100, data.config.HEIGHT * 0.4 - 50))

            graphics.drawText(buf, data.translate("submit"), 100, 50 - 15, size=20, formatting="center")
            graphics.drawText(buf, data.translate("score"), 100, 50 + 15, size=20, formatting="center")
            graphics.drawText(buf, data.translate("exit"), 100 + data.config.WIDTH * 0.3, 50, size=20, formatting="center")

            buf.fill((255, 255, 255, 255 - self.transitionTimer * 2), special_flags=pygame.BLEND_RGBA_MULT)
            display.blit(buf, (data.config.WIDTH * 0.35 - 100, data.config.HEIGHT * 0.4 - 50))
            self.transitionTimer += 2

        elif self.transitionTimer < 256:
            buf = display.copy()

            self.menu_list.draw(buf)

            graphics.drawText(buf, data.translate("name"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4, size=40, color=self.color, formatting="center")
            graphics.drawText(buf, data.translate("submit"), data.config.WIDTH * 0.5 + 225, data.config.HEIGHT * 0.55, size=20 , formatting="center")

            buf.set_alpha(2 * self.transitionTimer - 256, pygame.RLEACCEL)
            display.blit(buf, (0, 0))
            self.transitionTimer += 2

        else:
            self.menu_list.draw(display)

            graphics.drawText(display, data.translate("name"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.4, size=40, color=self.color, formatting="center")
            graphics.drawText(display, data.translate("submit"), data.config.WIDTH * 0.5 + 225, data.config.HEIGHT * 0.55, size=20 , formatting="center")

    def respondToUserInput(self, event):
        if self.transitionTimer < 64:
            return self

        for e in self.menu_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED \
            or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN \
            and self.menu_list.buttons[0].active == True):

                transitionTimer = 0
                display = pygame.display.get_surface()
                static = display.copy()

                blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
                blackness.fill(0x000000)

                while transitionTimer <= 255:
                    display.blit(static, (0, 0))

                    blackness.set_alpha(transitionTimer, pygame.RLEACCEL)
                    display.blit(blackness, (0, 0))

                    transitionTimer += 1
                    pygame.display.flip()

                ranking = data.load("ranking")

                ranking.append((self.menu_list.getText("name"), self.score))
                ranking = sorted(ranking, key=itemgetter(1), reverse=True)[0:10]

                data.save(ranking, "ranking")

                return screen.Ranking(fadin=True, showCredits=self.color == 0x262626)

        return self

    def update(self):
        if len(self.menu_list.getText("name")) >= 3:
            self.menu_list.buttons[0].active = True
        else: self.menu_list.buttons[0].active = False

