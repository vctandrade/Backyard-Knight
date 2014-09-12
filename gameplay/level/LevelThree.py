import gameplay

class LevelThree(object):

    def __init__(self, player):

        self.player = player
        self.player.world = self
        self.player.interactibles = set()
        self.camera = gameplay.Camera(120, 464)

        self.player.sprite.x, self.player.sprite.y = 120, 464
        self.player.xVel, self.player.yVel = 0, 0
        self.player.invincibility = 0

        sketch = [
                  " ############################################################################################################## ",
                  "##............................................................................................................##",
                  "#..............................................................................................................#",
                  "#..............................................................................................................#",
                  "#..............................................................................................................#",
                  "#..............................................................................................................#",
                  "#..............................................................................................................#",
                  "#..............................................................................................................#",
                  "###################........................######.........######################################################",
                  "######.....................................######............#",
                  "####.....................#############.....######...#........#",
                  "##...................#################..............####.....#",
                  "#.................####################..............#........#",
                  "#..............#######################..............#........#",
                  "#..........###########################..............#.....####",
                  "#...................................................#........#",
                  "########............................................#........#",
                  "#####...............................................####.....#",
                  "#...................................................#........#",
                  "#...................................................#........#",
                  "#...................................................#.....####",
                  "#......##############################################........#",
                  "##..............................................#####........#",
                  "##................................................######.....#",
                  "###..........................................................#",
                  "####.........................................................#",
                  "######....................................................####",
                  "##############################################################",
                  ]

        self.map = list()
        self.next = None

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()

        self.entities.append(gameplay.entity.Chest(self, [98, 220]))
        self.entities.append(gameplay.entity.Chest(self, [1468, 220]))

        self.entities.append(gameplay.entity.Golem(self, [280, 148], side=1))
        self.entities.append(gameplay.entity.Skeleton(self, [1468, 580]))
        self.entities.append(gameplay.entity.Skeleton(self, [968, 580], side=1))
        self.entities.append(gameplay.entity.Slime(self, [568, 670]))
        self.entities.append(gameplay.entity.Beholder(self, [988, 800]))

        self.entities.append(gameplay.entity.Door(self, [3368, 256], gameplay.level.Boss))

        self.entities.append(gameplay.entity.Spike(self, [1892, 856], "up", startTime=100))
        self.entities.append(gameplay.entity.Spike(self, [1754, 756], "up", startTime=80))
        self.entities.append(gameplay.entity.Spike(self, [1892, 656], "up", startTime=60))
        self.entities.append(gameplay.entity.Spike(self, [1754, 556], "up", startTime=40))
        self.entities.append(gameplay.entity.Spike(self, [1892, 464], "up", startTime=20))
        self.entities.append(gameplay.entity.Spike(self, [1754, 364], "up"))

        self.entities.append(gameplay.entity.Spike(self, [2200, 270], "up", waitTime=96))
        self.entities.append(gameplay.entity.Spike(self, [2300, 004], "down", waitTime=132))
        self.entities.append(gameplay.entity.Spike(self, [2400, 270], "up", waitTime=156))
        self.entities.append(gameplay.entity.Spike(self, [2500, 004], "down", waitTime=4))
        self.entities.append(gameplay.entity.Spike(self, [2600, 270], "up", waitTime=128))
        self.entities.append(gameplay.entity.Spike(self, [2700, 004], "down", waitTime=200))
        self.entities.append(gameplay.entity.Spike(self, [2800, 270], "up", waitTime=136))
        self.entities.append(gameplay.entity.Spike(self, [2900, 004], "down", waitTime=160))
        self.entities.append(gameplay.entity.Spike(self, [3000, 270], "up", waitTime=124))
        self.entities.append(gameplay.entity.Spike(self, [3100, 004], "down", waitTime=194))



    def draw(self, display):

        offset = self.camera.convert()

        y = 0
        for line in self.map:
            x = 0
            for tile in line:
                drawPos = (x - offset[0], y - offset[1])
                display.blit(tile.getSprite(), drawPos)
                x += gameplay.tile.size
            y += gameplay.tile.size

        for entity in self.entities:
            entity.draw(display, offset)

        self.player.draw(display, offset)

    def update(self):
        for entity in self.entities:
            entity.update()
            if entity.dead: self.entities.remove(entity)

        self.player.update()
        self.camera.update(self.player.sprite)


