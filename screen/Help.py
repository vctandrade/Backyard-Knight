import graphics
import gameplay
import pygame
import screen
import data

class Help(object):

    def __init__(self, origin, camera=None):
        self.origin = origin

        self.help_list = graphics.userInterface.Interface()
        self.image = 0

        self.help_list.addButton(0, "arrow_back.png", data.config.WIDTH * 0.1, data.config.HEIGHT * 0.1, mask="arrow_leftMask.png")
        self.help_list.addButton(1, "arrow_left.png", data.config.WIDTH * 0.4, data.config.HEIGHT * 0.9, mask="arrow_leftMask.png")
        self.help_list.addButton(2, "arrow_right.png", data.config.WIDTH * 0.6, data.config.HEIGHT * 0.9, mask="arrow_rightMask.png")
        self.help_list.addButton(3, "door-button.png", data.config.WIDTH * 0.5, data.config.HEIGHT * 0.35, mask="door-mask.png", active=False, visible=False)

        self.shadow = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
        self.shadow.set_alpha(224, pygame.RLEACCEL)

        self.camera = camera

    def displayOutput(self, display):
        textColor = 0x161616
        menuNum = 3

        if self.origin is not screen.Menu:
            display.blit(self.shadow, (0, 0))
            textColor = 0xE0E0E0
            menuNum = 2
        else: display.fill((0, 90, 150))

        if self.image % menuNum == 0:
            display.blit(data.getResource("help_esc.png"), (data.config.WIDTH * 0.4 - 200, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("help_Z.png"), (data.config.WIDTH * 0.4 - 200, data.config.HEIGHT * 0.25 + 80))
            display.blit(data.getResource("help_X.png"), (data.config.WIDTH * 0.4 - 200, data.config.HEIGHT * 0.25 + 80 * 2))
            display.blit(data.getResource("help_C.png"), (data.config.WIDTH * 0.4 - 200, data.config.HEIGHT * 0.25 + 80 * 3))

            display.blit(data.getResource("help_up.png"), (data.config.WIDTH * 0.6 - 100, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("help_down.png"), (data.config.WIDTH * 0.6 - 100, data.config.HEIGHT * 0.25 + 80))
            display.blit(data.getResource("help_left.png"), (data.config.WIDTH * 0.6 - 100, data.config.HEIGHT * 0.25 + 80 * 2))
            display.blit(data.getResource("help_right.png"), (data.config.WIDTH * 0.6 - 20, data.config.HEIGHT * 0.25 + 80 * 2))

            graphics.drawText(display, data.translate("controls"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, color=textColor, size=40, formatting="center")

            graphics.drawText(display, data.translate("pause"), data.config.WIDTH * 0.4 - 120, data.config.HEIGHT * 0.25 + 20, color=textColor, size=20)
            graphics.drawText(display, data.translate("jump"), data.config.WIDTH * 0.4 - 120, data.config.HEIGHT * 0.25 + 80 + 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("attack"), data.config.WIDTH * 0.4 - 120, data.config.HEIGHT * 0.25 + 80 * 2 + 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("use item"), data.config.WIDTH * 0.4 - 120, data.config.HEIGHT * 0.25 + 80 * 3 + 25, color=textColor, size=20)

            graphics.drawText(display, data.translate("open"), data.config.WIDTH * 0.6 - 20, data.config.HEIGHT * 0.25 + 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("crouch"), data.config.WIDTH * 0.6 - 20, data.config.HEIGHT * 0.25 + 80 + 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("move"), data.config.WIDTH * 0.6 + 60, data.config.HEIGHT * 0.25 + 80 * 2 + 25, color=textColor, size=20)

            graphics.drawText(display, data.translate("jump higher"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.65 + 60, color=textColor, size=18, formatting="center")

        elif self.image % menuNum == 1:
            display.blit(data.getResource("items.png")[0], (data.config.WIDTH * 0.6 + 150, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[1], (data.config.WIDTH * 0.6 + 150 - 48, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[2], (data.config.WIDTH * 0.6 + 150 - 48 * 2, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[3], (data.config.WIDTH * 0.6 + 150 - 48 * 3, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[4], (data.config.WIDTH * 0.6 + 150 - 48 * 4, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[5], (data.config.WIDTH * 0.6 + 150 - 48 * 5, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[6], (data.config.WIDTH * 0.6 + 150 - 48 * 6, data.config.HEIGHT * 0.25))
            display.blit(data.getResource("items.png")[7], (data.config.WIDTH * 0.6 + 150 - 48 * 7, data.config.HEIGHT * 0.25))

            display.blit(data.getResource("items.png")[8], (data.config.WIDTH * 0.6 + 150, data.config.HEIGHT * 0.25 + 80))
            display.blit(data.getResource("items.png")[9], (data.config.WIDTH * 0.6 + 150 - 48, data.config.HEIGHT * 0.25 + 80))

            display.blit(data.getResource("items.png")[16], (data.config.WIDTH * 0.6 + 150, data.config.HEIGHT * 0.25 + 80 * 2))
            display.blit(data.getResource("items.png")[17], (data.config.WIDTH * 0.6 + 150 - 48, data.config.HEIGHT * 0.25 + 80 * 2))
            display.blit(data.getResource("items.png")[18], (data.config.WIDTH * 0.6 + 150 - 48 * 2, data.config.HEIGHT * 0.25 + 80 * 2))

            display.blit(data.getResource("items.png")[11], (data.config.WIDTH * 0.6 + 150, data.config.HEIGHT * 0.25 + 80 * 3))
            display.blit(data.getResource("chest.png")[0], (data.config.WIDTH * 0.3 - 200, data.config.HEIGHT * 0.55 - 120))

            graphics.drawText(display, data.translate("items"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=40, color=textColor, formatting="center")

            graphics.drawText(display, data.translate("chest1"), data.config.WIDTH * 0.3 - 250, data.config.HEIGHT * 0.55, color=textColor, size=20)
            graphics.drawText(display, data.translate("chest2"), data.config.WIDTH * 0.3 - 250, data.config.HEIGHT * 0.55 + 50, color=textColor, size=20)
            graphics.drawText(display, data.translate("chest3"), data.config.WIDTH * 0.3 - 250, data.config.HEIGHT * 0.55 + 100, color=textColor, size=20)
            graphics.drawText(display, data.translate("chest4"), data.config.WIDTH * 0.3 - 250, data.config.HEIGHT * 0.55 + 150, color=textColor, size=15)
            graphics.drawText(display, data.translate("food"), data.config.WIDTH * 0.6 + 150 + 80, data.config.HEIGHT * 0.25 + 24, color=textColor, size=20)
            graphics.drawText(display, data.translate("potions"), data.config.WIDTH * 0.6 + 150 + 80, data.config.HEIGHT * 0.25 + 80 + 24, color=textColor, size=20)
            graphics.drawText(display, data.translate("weapons"), data.config.WIDTH * 0.6 + 150 + 80, data.config.HEIGHT * 0.25 + 80 * 2 + 24, color=textColor, size=20)
            graphics.drawText(display, data.translate("bomb"), data.config.WIDTH * 0.6 + 150 + 80, data.config.HEIGHT * 0.25 + 80 * 3 + 24, color=textColor, size=20)

        elif self.image % menuNum == 2:
            graphics.drawText(display, data.translate("test"), data.config.WIDTH * 0.5, data.config.HEIGHT * 0.1, size=40, color=textColor, formatting="center")

            graphics.drawText(display, data.translate("test1"), data.config.WIDTH * 0.5 - 320, data.config.HEIGHT * 0.62 - 75, color=textColor, size=20)
            graphics.drawText(display, data.translate("test2"), data.config.WIDTH * 0.5 - 320, data.config.HEIGHT * 0.62 - 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("test3"), data.config.WIDTH * 0.5 - 320, data.config.HEIGHT * 0.62 + 25, color=textColor, size=20)
            graphics.drawText(display, data.translate("test4"), data.config.WIDTH * 0.5 - 320, data.config.HEIGHT * 0.62 + 75, color=textColor, size=20)


        self.help_list.draw(display)

    def respondToUserInput(self, event):
        for e in self.help_list.handle(event):
            if e.type == graphics.userInterface.BUTTONCLICKED:
                    if e.button == 0:
                        if self.origin == screen.Pause:
                            return self.origin(self.camera)
                        return self.origin()
                    if e.button == 1 :
                        self.image -= 1
                    if e.button == 2:
                        self.image += 1

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

                        return screen.Gameplay(gameplay.level.Tutorial)

                    if self.origin is screen.Menu and self.image % 3 == 2:
                        self.help_list.buttons[3].active = True
                        self.help_list.buttons[3].visible = True
                    else:
                        self.help_list.buttons[3].active = False
                        self.help_list.buttons[3].visible = False

        return self

    def update(self):
        pass
