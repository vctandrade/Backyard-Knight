import gameplay

class Tutorial(object):

    def __init__(self, player):

        self.player = player
        self.player.world = self
        self.player.interactibles = set()
        self.camera = gameplay.Camera(120, 208)

        self.player.sprite.x, self.player.sprite.y = 120, 208
        self.player.xVel, self.player.yVel = 0, 0
        self.player.invincibility = 0
        self.player.health = 5
        self.player.score = -1

        self.freezeTimer = -64

        sketch = [
                  "########################################################################",
                  "#.............................##.......................................#",
                  "#.............................##.......................................#",
                  "#.............................##.......................................#",
                  "#.............................##.......................................#",
                  "#.............................##...##..................................#",
                  "#........................##........##..................................#",
                  "#........................##........##..................................#",
                  "########################################################################",
                  ]

        self.map = list()
        self.next = None

        for line in sketch:
            newLine = list()

            for char in line:
                newLine.append(gameplay.tile.translate(char))

            self.map.append(newLine)

        self.entities = list()
        self.particles = list()

        self.entities.append(gameplay.entity.Chest(self, [300, 220], gameplay.item.Food()))
        self.entities.append(gameplay.entity.Chest(self, [450, 220], gameplay.item.HealthPotion()))
        self.entities.append(gameplay.entity.Chest(self, [600, 220], gameplay.item.InvincibilityPotion()))

        self.entities.append(gameplay.entity.Dummy(self, [1400, 220]))

        self.entities.append(gameplay.entity.Chest(self, [1550, 220], gameplay.item.Hammer()))
        self.entities.append(gameplay.entity.Chest(self, [1700, 220], gameplay.item.Spear()))
        self.entities.append(gameplay.entity.Chest(self, [1850, 220], gameplay.item.Bomb()))

        self.entities.append(gameplay.entity.Door(self, (2100, 256), "Victor is awesome!"))

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

        for particle in self.particles:
            particle.draw(display, offset)

    def update(self):
        for entity in self.entities:
            entity.update()
            if entity.dead: self.entities.remove(entity)

        for particle in self.particles:
            particle.update()
            if particle.dead: self.particles.remove(particle)

        self.player.update()
        self.camera.update(self.player.sprite)
