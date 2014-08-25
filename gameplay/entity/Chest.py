import data
import graphics
import gameplay
import random
class Chest(object):
    
    def __init__(self,world,pos):
        
        self.world = world
        self.animation = graphics.AnimationInfo()
        self.sprite = graphics.Sprite(0, "chest.png", (0, 0))
        
        self.sprite.x, self.sprite.y = pos
        self.state = "closed"
        
        self.dead = False
    
    
    def draw(self,display, offset=(0, 0)):
        
        if self.state == "closed":
            self.sprite.index = 0
        if self.state == "open":
            self.sprite.index =  1 if self.animation.timer < 48 else 2 if self.animation.timer < 56 else 3 if self.animation.timer < 64 else 4
        if self.state == "alreadyOpen":
            self.sprite.index =  4
    
        self.animation.timer += 1
        self.animation.animate(self.sprite)

        self.sprite.draw(display, offset)
    
    def playerClose(self):
        return abs(self.sprite.y - self.world.player.sprite.y) < 30 and abs(self.sprite.x - self.world.player.sprite.x) < 30
    
    def RandomizeItem(self):
        num = random.randint(0,100)
        if num in range(0,4):
            return num, gameplay.item.Sword()
        if num in range(5,9):
            return num, gameplay.item.Spear()
        if num in range(10,14):
            return num, gameplay.item.Hammer()
        if num in range(15,24):
            return num, gameplay.item.Food()
        if num in range(25,29):
            return num, gameplay.item.HealthPotion()
        if num in range(30,33):
            return num, gameplay.item.InvincibilityPotion()
        if num in range(34,38):
            return num, gameplay.item.Bomb()
        else:
            return num, gameplay.item.Food()
    
    def openChest(self):
        if self.playerClose() and self.state == "closed" :
            self.state = "open"
            
            n, item = self.RandomizeItem()
            print n
            if n <14:
                self.world.player.weapon = item
            else:
                self.world.player.item = item    
            self.animation.timer = 0
            
    def collidedWith(self,origin):
        pass
    def living(self):
        return False
                   
    def update(self):       
        if self.state == "open":
            self.state = "alreadyOpen"

