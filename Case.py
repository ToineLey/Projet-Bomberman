from Terrain import Terrain


class Case:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.terrain = t
        self.bomb = None
        self.explosion = 0
        self.player = None

    def explode(self):
        if self.terrain == Terrain.BRIQUE:
            self.terrain = Terrain.VIDE
        elif self.player != None:
            self.player.dead = True
        self.bomb = None
        self.explosion -= 1

    def est_libre(self):
        return self.terrain == Terrain.VIDE and self.player == None

    def __str__(self):
        # Ces lignes servent uniquement pour les tests (pour que cela soit plus visuel)
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0 and self.player is None and self.bomb is None and self.explosion == 0:
            return '  '
        elif self.terrain == 2:
            return '██'
        elif self.bomb is not None:
            return '!!'
        elif self.player is not None:
            return '()'
        elif self.explosion != 0:
            return '**'
