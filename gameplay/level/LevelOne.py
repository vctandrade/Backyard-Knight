import gameplay

class LevelOne(object):

    def __init__(self, player):

        self.player = player
        self.player.world = self
        self.player.interactibles = set()
        self.camera = gameplay.Camera(106, 656)

        self.player.sprite.x, self.player.sprite.y = 106, 656
        self.player.xVel, self.player.yVel = 0, 0
        self.player.invincibility = 0

        sketch = [
                  "                ############################                     ",
                  "               ##.....................#########################  ",
                  "              ##.......................#######...............### ",
                  "             ##........................######.................###",
                  "            ##.................#############...................##",
                  "            #...................................................#",
                  "            #...................................................#",
                  "            #............###....................................#",
                  "            #...........#####...................................#",
                  "           ################################################.....#",
                  "         #######################.........................##.....#",
                  "       ####........#..........................................###",
                  "     #####.........#..........................................###",
                  "   ######.....................................................###",
                  " ########...................................................#####",
                  "##############..............................................#####",
                  "###########......###############....###....###....###.....#######",
                  "#................###############..........................#######",
                  "#...............################..........................#######",
                  "#...............################.........................########",
                  "#..............#################.........................########",
                  "#..............#################.........................########",
                  "#################################################################",
                  ]

        self.map = list()
        self.next = None

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()

        self.entities.append(gameplay.entity.Chest(self, (380, 444)))
        self.entities.append(gameplay.entity.Chest(self, (1120, 92)))

        self.entities.append(gameplay.entity.Skeleton(self, (920, 480)))
        self.entities.append(gameplay.entity.Slime(self, (1200, 600)))
        self.entities.append(gameplay.entity.Slime(self, (1300, 600)))
        self.entities.append(gameplay.entity.Slime(self, (1400, 600)))
        self.entities.append(gameplay.entity.Slime(self, (1500, 600)))
        self.entities.append(gameplay.entity.Slime(self, (1600, 600)))
        self.entities.append(gameplay.entity.Golem(self, (1680, 200), side=1))
        self.entities.append(gameplay.entity.Skeleton(self, (1120, 240), side=1))

        self.entities.append(gameplay.entity.Door(self, (600, 286), gameplay.level.LevelTwo))

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
