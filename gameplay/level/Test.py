import gameplay
import graphics

class Test(object):

    def __init__(self):
        sketch = [
                  "##############################################",
                  "###############......#########################",
                  "##.#.#.#.#.#.#...............................#",
                  "##..........................#.......#........#",
                  "##...........................................#",
                  "##...........................................#",
                  "##...........................................#",
                  "##..##############...#.#.#.#.#.#.#.#.#.#.....#",
                  "##....#................................##....#",
                  "##....#......................................#",
                  "####..#..........#####.......................#",
                  "#.....#....................................###",
                  "##....#....................................###",
                  "#...###............................##......###",
                  "##..#.................###..........##.....####",
                  "#.........................................####",
                  "##.....................................#..####",
                  "##############################################",
                  ]

        self.map = list()

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()

        self.entities.append(gameplay.entity.Slime(self, [412, 500]))
        self.entities.append(gameplay.entity.Slime(self, [812, 200]))

    def draw(self, display, offset=(0, 0)):
        y = 0
        for line in self.map:
            x = 0
            for tile in line:
                drawPos = graphics.drawPos(x - offset[0], y - offset[1])
                display.blit(tile.getSprite(), drawPos)
                x += gameplay.tile.size
            y += gameplay.tile.size

        for entity in self.entities:
            entity.draw(display, offset)

    def update(self):
        for entity in self.entities:
            entity.update()
