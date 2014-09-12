import gameplay
import graphics
import keyboard
import screen
import pygame
import data

class Gameplay(object):

    def __init__(self, level=gameplay.level.Boss):
        data.playMusic("pull-me-under.ogg")
        pygame.mouse.set_visible(False)

        self.world = level(gameplay.entity.Player())
        keyboard.setMultiKeys(pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_x)

        self.transitionTimer = 1
        self.overlay = None

        self.start = pygame.time.get_ticks()
        self.startPause = 0
        self.timer = 0

    def displayOutput(self, display):
        if type(self.overlay) != screen.Dead or self.overlay.transitionTimer < 128:
            self.world.draw(display)

        for i in range(self.world.player.maxHealth / 2 + self.world.player.maxHealth % 2):
            fullHeart = data.getResource("life.png")[0].copy()
            halfHeart = data.getResource("life.png")[1].copy()
            noHeart = data.getResource("life.png")[2].copy()

            if hasattr(self.world, "backyardTimer"):
                fullHeart.set_alpha(384 - self.world.backyardTimer, pygame.RLEACCEL)
                halfHeart.set_alpha(384 - self.world.backyardTimer, pygame.RLEACCEL)
                noHeart.set_alpha(384 - self.world.backyardTimer, pygame.RLEACCEL)

            if self.world.player.health >= 2 + 2 * i:
                display.blit(fullHeart, (24 + i * 48, 32))
            if self.world.player.health == 1 + 2 * i:
                display.blit(halfHeart, (24 + i * 48, 32))
            if self.world.player.health < 1 + 2 * i:
                display.blit(noHeart, (24 + i * 48, 32))

        weapon = data.getResource("weapon_box.png").copy().convert()
        item = data.getResource("item_box.png").copy().convert()

        weapon.set_alpha(255)
        item.set_alpha(255)

        if self.world.player.flashTimer > 0:
            if self.world.player.flashMode == "weapon":
                weapon = data.getResource("changed_box.png").copy()
            else: item = data.getResource("changed_box.png").copy()
            self.world.player.flashTimer -= 1

        if self.world.player.item != None:
            self.world.player.item.icon.draw(item, (-30, -30))
        self.world.player.weapon.icon.draw(weapon, (-30, -30))

        if hasattr(self.world, "backyardTimer"):
            weapon.set_alpha(384 - self.world.backyardTimer, pygame.RLEACCEL)
            item.set_alpha(384 - self.world.backyardTimer, pygame.RLEACCEL)

        display.blit(weapon, (data.config.WIDTH - 152, 24))
        display.blit(item, (data.config.WIDTH - 80, 24))

        if self.world.player.score >= 0:
            graphics.drawText(display, "%.6d" % self.world.player.score, data.config.WIDTH / 2, 48, 0xFFEE00, 30, "center", "Time_10x10.png")

        if not hasattr(self.world, "freezeTimer") or (self.world.freezeTimer / 16) % 4:
            seconds = min(self.timer / 1000, 3599)
            minutes = seconds / 60

            timeString = "%.2d:%.2d" % (minutes % 60, seconds % 60)
            graphics.drawText(display, timeString, data.config.WIDTH - 180, data.config.HEIGHT - 40, 0x0FFFFFF, 30, font="Time_10x10.png")

        if not self.overlay and hasattr(self.world, "freezeTimer"):
            if self.world.freezeTimer >= 0:
                self.world.freezeTimer += 1

        if self.transitionTimer >= 0 or self.world.next:
            blackness = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
            blackness.set_alpha(255 - self.transitionTimer % 64 * 4, pygame.RLEACCEL)

            display.blit(blackness, (0, 0))

        if self.overlay: self.overlay.displayOutput(display)

    def respondToUserInput(self, event):
        if self.overlay:
            self.overlay = self.overlay.respondToUserInput(event)

            if self.overlay == None:
                pygame.mouse.set_visible(False)
                return self

            if type(self.overlay) in (screen.Gameplay, screen.Menu):
                return self.overlay

        if not self.overlay or type(self.overlay) == screen.Win:
            if self.world.next == None and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: self.world.player.moveRight()
                if event.key == pygame.K_LEFT: self.world.player.moveLeft()
                if event.key == pygame.K_DOWN: self.world.player.crouch()
                if event.key == pygame.K_UP: self.world.player.interact()
                if event.key == pygame.K_z: self.world.player.jump()
                if event.key == pygame.K_x: self.world.player.attack()
                if event.key == pygame.K_c: self.world.player.useItem()

                if event.key == pygame.K_ESCAPE and not self.world.player.dead:
                    if hasattr(self.world, "backyardTimer"):
                        return self

                    self.startPause = pygame.time.get_ticks()
                    self.overlay = screen.Pause(self.world.camera)

                    pygame.mouse.set_visible(True)

                if type(self.world) == gameplay.level.Tutorial:
                    if event.key == pygame.K_UP and len(self.world.player.interactibles) == 1:
                        entity = self.world.player.interactibles.pop()
                        self.world.player.interactibles.add(entity)

                        if type(entity) == gameplay.entity.Door:

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

                            pygame.mouse.set_visible(True)
                            return screen.Menu(fadin=True)

        return self

    def update(self):
        if data.getMusic() == "win-intro.ogg" and not self.world.player.dead:
            if not pygame.mixer.music.get_busy():
                data.playMusic("win-main.ogg")

        if type(self.overlay) == screen.Dead:
            self.world.update()

        if self.overlay:
            self.overlay.update()
            if type(self.overlay) != screen.Win:
                return

        if self.world.player.dead:
            pygame.mixer.music.fadeout(1024)
            if self.world.player.animation.timer >= 72:
                pygame.mouse.set_visible(True)
                self.overlay = screen.Dead()

        if self.transitionTimer < 0:
            if self.world.next != None:
                if self.world.next == gameplay.level.Boss:
                    pygame.mixer.music.fadeout(1024)
                self.transitionTimer = 64

        if self.transitionTimer == 0:
            self.world = self.world.next(self.world.player)

        if self.world.next == None:
            if self.transitionTimer >= 0:
                self.transitionTimer += 2
            if self.transitionTimer == 64:
                self.transitionTimer = -1
            self.world.update()

        self.transitionTimer = max(self.transitionTimer - 1, -1)

        if hasattr(self.world, "backyardTimer"):
            if (self.world.freezeTimer / 16) % 4:
                self.world.freezeTimer = -16

            if not hasattr(self, "score"):
                self.score = 5 * 60 * 1000 * 10 / self.timer
                self.timeDown = self.timer / (self.score / 7.0)

            elif self.score > 0:
                if self.score % 42 < 7: data.playSound("orb.ogg")
                self.timer = max(self.timer - self.timeDown, 0)
                self.world.player.score += min(self.score, 7)
                self.score -= 7

            else:
                if self.world.backyardTimer >= 384 \
                and type(self.overlay) != screen.Win:
                    pygame.mouse.set_visible(True)
                    self.overlay = screen.Win(self.world.player.score)
                self.world.freezeTimer = -64

        if self.world.next or self.world.player.health <= 0 or hasattr(self.world, "freezeTimer"):
            if self.startPause == 0:
                self.startPause = pygame.time.get_ticks()
            return

        if self.startPause != 0:
            self.start += pygame.time.get_ticks() - self.startPause

        self.timer = (pygame.time.get_ticks() - self.start)

        self.startPause = 0
