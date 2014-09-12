import graphics
import screen
import data

class Ranking(object):

    def __init__(self):
        self.ranking_list = graphics.userInterface.Interface()

        self.ranking_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.ranking_list.addSlider(1, "slider.png", "slidermask.png", (0, 100), 0, data.config.WIDTH * 0.9 , data.config.HEIGHT * 0.5, vertical=True)

        try: self.list = data.load("ranking")
        except: data.save([], "ranking")

        self.list = data.load("ranking")

    def displayOutput(self, display):
        self.ranking_list.draw(display)

        purple = 0x7018cb

        for i in range(1, len(self.list) + 1):

            y = (data.config.HEIGHT * 0.5 * i / 3.0) - self.ranking_list.sliders[1].value * len(self.list)
            if y > data.config.HEIGHT * 0.12:
                display.blit(data.getResource("ranking_pos.png"), (data.config.WIDTH * 0.15, y))
                display.blit(data.getResource("ranking_slot.png"), (data.config.WIDTH * 0.25, y))
                display.blit(data.getResource("ranking_score.png"), (data.config.WIDTH * 0.64, y))

                graphics.drawText(display, str(i), data.config.WIDTH * 0.15 + 50, data.config.HEIGHT * 0.5 * i / 3.0 + 50 - self.ranking_list.sliders[1].value * len(self.list), size=40, color=purple, formatting="center")
                graphics.drawText(display, self.list[i - 1][0], data.config.WIDTH * 0.25 + 20, data.config.HEIGHT * 0.5 * i / 3.0 + 50 - self.ranking_list.sliders[1].value * len(self.list), size=20, color=purple)
                graphics.drawText(display, str(self.list[i - 1][1]), data.config.WIDTH * 0.64 + 20, data.config.HEIGHT * 0.5 * i / 3.0 + 50 - self.ranking_list.sliders[1].value * len(self.list), size=20, color=purple)



        graphics.drawText(display, data.translate("ranking"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=50, color=0xffffff, formatting="center")

    def respondToUserInput(self, event):
        for e in self.ranking_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                return screen.Menu()

        return self

    def update(self):
        pass


