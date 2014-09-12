import graphics
import pygame
import screen
import data

class Ranking(object):

    def __init__(self, fadin=False, showCredits=True):

        try: self.list = data.load("ranking")
        except: data.save([], "ranking")
        self.list = data.load("ranking")

        self.ranking_list = graphics.userInterface.Interface()
        self.ranking_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.ranking_list.addSlider(1, "slider.png", "slidermask.png", (0, 1000), 0, data.config.WIDTH * 0.75 + 180, data.config.HEIGHT * 0.55, vertical=True, visible=len(self.list) > 5)

        self.fadin = 256 if fadin else -1
        self.showCredits = showCredits

    def displayOutput(self, display):
        display.fill(0x101010)
        display.blit(data.getResource("ranking.png"), (data.config.WIDTH * 0.5 - 350 - 8, data.config.HEIGHT * 0.55 - 272))

        self.ranking_list.draw(display)

        purple = 0x7018cb
        buff = display.copy()

        if len(self.list) == 0:
            graphics.drawText(buff, data.translate("empty"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.55, size=30, color=0x303030, formatting="center")

        for i in range(0, len(self.list)):

            y = data.config.HEIGHT * 0.55 - 218 + i * 110 - self.ranking_list.getSliderValue(1) * max(0, len(self.list) - 5) * 110 / 1000

            buff.blit(data.getResource("ranking_pos.png"), (data.config.WIDTH * 0.5 - 350, y - 46))
            buff.blit(data.getResource("ranking_slot.png"), (data.config.WIDTH * 0.5 - 240, y - 46))
            buff.blit(data.getResource("ranking_score.png"), (data.config.WIDTH * 0.5 + 160, y - 46))

            if data.config.HEIGHT * 0.55 - 276 < y < data.config.HEIGHT * 0.55 + 272 + 15:
                graphics.drawText(buff, str(i + 1), data.config.WIDTH * 0.5 - 300, y, size=30, color=purple, formatting="center")
                graphics.drawText(buff, self.list[i][0], data.config.WIDTH * 0.5 - 228, y, size=20, color=purple)
                graphics.drawText(buff, "%4d" % self.list[i][1], data.config.WIDTH * 0.5 + 160 + 100, y, size=20, color=purple, formatting="center")

        display.blit(buff, (data.config.WIDTH * 0.5 - 350, data.config.HEIGHT * 0.55 - 268), ((data.config.WIDTH * 0.5 - 350, data.config.HEIGHT * 0.55 - 268), (710, 540)))

        display.blit(data.getResource("separator.png"), (data.config.WIDTH * 0.5 - 350 - 8, data.config.HEIGHT * 0.55 - 276))
        display.blit(data.getResource("separator.png"), (data.config.WIDTH * 0.5 - 350 - 8, data.config.HEIGHT * 0.55 + 272))

        if self.fadin > 0:
            blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
            blackness.set_alpha(self.fadin, pygame.RLEACCEL)

            display.blit(blackness, (0, 0))
            self.fadin -= 4

        graphics.drawText(display, data.translate("ranking"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=40, color=0xffffff, formatting="center")

    def respondToUserInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 4:
                self.ranking_list.sliders[1].value = max(self.ranking_list.sliders[1].value - 50, self.ranking_list.sliders[1].left)
            if event.button == 5:
                self.ranking_list.sliders[1].value = min(self.ranking_list.sliders[1].value + 50, self.ranking_list.sliders[1].right)

        for e in self.ranking_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                if self.fadin >= 0:

                    if not self.showCredits: pygame.mixer.music.fadeout(1024)


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

                    return screen.Credits(fadin=True) if self.showCredits else screen.Menu(fadin=True)

                return screen.Menu()

        return self

    def update(self):
        pass


