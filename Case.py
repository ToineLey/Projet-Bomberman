from Terrain import Terrain

class Case:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.terrain = t
        self.bomb = False
        self.explosion = 0
        self.player = None

    def explode(self):
        if self.terrain == Terrain.BRIQUE:
            self.terrain = Terrain.VIDE
        elif self.player != None:
            self.player.dead = True
        self.bomb = None
        self.explosion -= 1