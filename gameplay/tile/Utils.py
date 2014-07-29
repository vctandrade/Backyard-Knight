import gameplay

size = 32

tileMap = {
           '.': lambda: gameplay.tile.Air(),
           '#': lambda: gameplay.tile.Dirt()
           }

def translate(symbol):
    return tileMap[symbol]()
