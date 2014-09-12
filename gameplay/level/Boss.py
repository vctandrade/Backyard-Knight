import gameplay
import pygame
import data

class Boss(object):

    def __init__(self, player):

        data.playMusic("a-violent-encounter.ogg")

        self.player = player
        self.player.world = self
        self.player.interactibles = set()
        self.camera = gameplay.Camera(816, 400)

        self.player.sprite.x, self.player.sprite.y = 816, 400
        self.player.xVel, self.player.yVel = 0, 0
        self.player.invincibility = 0

        towerSketch = [
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "        # . . . . . . . . . . . . . . . . #        ",
                        "        #.................................#        ",
                        "        ###.............................###        ",
                        "        ###################################        ",
                        "         #################################         ",
                        "          ###############################          ",
                        "           #############################           ",
                        "            ###########################            ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        "             #########################             ",
                        ]

        backyardSketch = [
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "                                                   ",
                        "          #  #                       #  #          ",
                        "          #  #                       #  #          ",
                        "          #  #                       #  #          ",
                        "          #  #                       #  #          ",
                        "          ###############################          ",
                        ]

        self.towerMap = list()
        self.backyardMap = list()
        self.next = None

        for line in towerSketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.towerMap.append(newLine)

        for line in backyardSketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.backyardMap.append(newLine)

        self.map = self.towerMap

        self.entities = list()

        self.entities.append(gameplay.entity.Boss(self, [816, 64]))

    def draw(self, display):
        offset = self.camera.convert()

        if not hasattr(self, "backyardTimer"):
            display.blit(data.getResource("night.png"), (data.config.WIDTH * 0.5 - 960, data.config.HEIGHT * 0.5 - 540))

            y = 0
            for line in self.towerMap:
                x = 0
                for tile in line:
                    drawPos = (x - offset[0], y - offset[1])
                    display.blit(tile.getSprite(), drawPos)
                    x += gameplay.tile.size
                y += gameplay.tile.size

        elif self.backyardTimer < 384:
            buf = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))
            buf.blit(data.getResource("night.png"), (data.config.WIDTH * 0.5 - 960, data.config.HEIGHT * 0.5 - 540))

            y = 0
            for line in self.towerMap:
                x = 0
                for tile in line:
                    drawPos = (x - offset[0], y - offset[1])
                    buf.blit(tile.getSprite(), drawPos)
                    x += gameplay.tile.size
                y += gameplay.tile.size

            buf.set_alpha(384 - self.backyardTimer, pygame.RLEACCEL)
            display.blit(buf, (0, 0))

        elif self.backyardTimer < 640:
            buf = pygame.Surface((data.config.WIDTH, data.config.HEIGHT))

            buf.blit(data.getResource("backyard.png"), (data.config.WIDTH * 0.5 - 960, data.config.HEIGHT * 0.85 - 1080 + 162))

            buf.set_alpha(self.backyardTimer - 384, pygame.RLEACCEL)
            display.blit(buf, (0, 0))

        else: display.blit(data.getResource("backyard.png"), (data.config.WIDTH * 0.5 - 960, data.config.HEIGHT * 0.85 - 1080 + 162))

        for entity in self.entities:
            entity.draw(display, offset)

        self.player.draw(display, offset)

    def update(self):
        for entity in self.entities:
            entity.update()
            if entity.dead: self.entities.remove(entity)

        self.player.update()

        relax = True
        lim = data.config.HEIGHT * 0.9
        adjust = [0, data.config.HEIGHT * 0.1 + 64]

        if hasattr(self, "backyardTimer"):
            lim = None
            relax = False

            adjust[0] += (self.player.sprite.x - 816) * min(self.backyardTimer, 128) / 128.0
            adjust[1] += (self.player.sprite.y - 596 + data.config.HEIGHT * 0.25) * min(self.backyardTimer, 128) / 128.0

            self.backyardTimer += 1

        self.camera.update(self.player.sprite, adjust, lim, relax)
