import gameplay

class Test(object):

    def __init__(self):

        self.camera = gameplay.Camera(540, 176)
        self.player = gameplay.entity.Player(self)

        self.player.sprite.x, self.player.sprite.y = 540, 176

        sketch = [
                  "#################################################",
                  "######################################################",
                  "##..................................................##",
                  "##..................................................##",
                  "##..................................................##",
                  "##..................................................##",
                  "##..................................................##",
                  "##..####################################............##",
                  "##.....................................##...........##",
                  "##..................................................##",
                  "####.........................................########",
                  "##..............................#..........######",
                  "##....###########################..........###",
                  "##..###........................##..........###",
                  "##..#...........................#.........####",
                  "##........................................####",
                  "##........................................####",
                  "##############################################",
                  ]

        self.map = list()
        self.next = None

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()

        self.entities.append(gameplay.entity.Chest(self, [750, 348]))
        self.entities.append(gameplay.entity.Chest(self, [1250, 508]))
        self.entities.append(gameplay.entity.Door(self, [1550, 320], gameplay.level.Boss))

        self.entities.append(gameplay.entity.Spike(self, [224, 224], "up"))

        self.entities.append(gameplay.entity.Beholder(self, [300, 320]))
        self.entities.append(gameplay.entity.Skeleton(self, [300, 480]))
        self.entities.append(gameplay.entity.Golem(self, [1150, 120]))
        self.entities.append(gameplay.entity.Slime(self, [1200, 500]))

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
