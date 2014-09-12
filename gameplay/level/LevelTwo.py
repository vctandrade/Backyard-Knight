import gameplay

class LevelTwo(object):

    def __init__(self, player):

        self.player = player
        self.player.world = self
        self.player.interactibles = set()
        self.camera = gameplay.Camera(480, 720)

        self.player.sprite.x, self.player.sprite.y = 480, 720
        self.player.xVel, self.player.yVel = 0, 0
        self.player.invincibility = 0

        sketch = [
                  "#############################################################################       ",
                  "#...........................................................................##",
                  "#............................................................................##",
                  "#.............................................................................##",
                  "#..............................................................................##",
                  "#...............................................................................#",
                  "#...............................................................................#",
                  "#############............................##################.....................#",
                  "           ####................................................####.............#",
                  "            ######..............................................................#",
                  "             ##########################...............................###########",
                  "             ########################...................................###",
                  "            ####.........................................................#",
                  "           ###...........................#####...........................#",
                  "          ###...........................##########.......................#",
                  "          ##...........................###############...................###",
                  "          #.............................###########......................######",
                  "          #..............................######............................########",
                  "          #......................######...................#####...............######",
                  "          #......................######......................###...................#",
                  "          #.................####..............................####.................#",
                  "          #.............########...............................####................#",
                  "          #.....................................................#####..............#",
                  "          #.......................................................######...........#",
                  "          ##########################################################################",
                  ]

        self.map = list()
        self.next = None

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()

        self.entities.append(gameplay.entity.Chest(self, [100, 188]))
        self.entities.append(gameplay.entity.Chest(self, [2550, 732]))

        self.entities.append(gameplay.entity.Skeleton(self, [1650, 700]))
        self.entities.append(gameplay.entity.Slime(self, [1400, 700]))
        self.entities.append(gameplay.entity.Slime(self, [1800, 700]))
        self.entities.append(gameplay.entity.Slime(self, [1650, 700]))

        self.entities.append(gameplay.entity.Golem(self, [800, 180], side=1))

        self.entities.append(gameplay.entity.Beholder(self, [2500, 700]))
        self.entities.append(gameplay.entity.Beholder(self, [1600, 180]))

        self.entities.append(gameplay.entity.Spike(self, [2115, 280], "up", waitTime=160))
        self.entities.append(gameplay.entity.Spike(self, [2043, 280], "up", waitTime=120))
        self.entities.append(gameplay.entity.Door(self, (2400, 320), gameplay.level.LevelThree))

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
