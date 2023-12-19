from random import randint
from Jules import *
from pip._vendor.platformdirs import user_videos_dir


class Grille:
    def __init__(self, l: int, h: int):
        self.hauteur = h
        self.largeur = l
        self.cases = [[j for j in range(l)] for _ in range(h)]

    def _remplir(self):
        def ot():
            return (
                n not in (0, self.largeur-1) and
                a not in (0, self.hauteur-1) and
                a % 2 != 0 and
                n % 2 != 0
            )

        def at():
            return (
                a in (0, 1) and
                n in (0, 1, self.largeur-2, self.largeur-1)
            )
        for a in range(len(self.cases)):
            for n in self.cases[a]:
                alea = randint(1, 100)
                if ot():
                    self.cases[a][n] = Case(a, n, Terrain.PILIER)
                elif at():
                    self.cases[a][n] = Case(a, n, Terrain.VIDE)
                else:
                    if alea <= 20:
                        self.cases[a][n] = Case(a, n, Terrain.VIDE)
                    else:
                        self.cases[a][n] = Case(a, n, Terrain.BRIQUE)

    def _affichage(self):
        t2 = []
        for a in range(len(self.cases)):
            t1 = []
            for el in self.cases[a]:
                t1.append(str(el))
            t2.append(t1)
        return t2

    def get(self, x: int, y: int):
        return self.cases[y][x]
"""
    def update_bomb(self):
        "compte a rebour des bombes"
        for bomb in all_bombs:
            bomb.rebour()
            if bomb.timer == 0:
                exploding_bomb.append(bomb)

    def update_explosions(self, x, y):
        "met a jour les cases en cours d'explosion autour de celle au coordonees x,y"

        case = self.get(x, y)
        i = 1

        ## Partie qui suit à optimiser ##

        while i <= Bomb.portee:
            current_case = self.get(x, y+i)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y-i)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x+i, y)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x-i, y)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break

    def bombs_explosion(self):
        "fait exploser les bombes"
        for bomb in self.exploding_bombs:
            self.update_explosions(bomb.x, bomb.y)
        self.explosions()

    def explosions(self):
        "explosions des cases"
        for case in get_explosions():
            case.explode()
"""

class Terrain:
    LISTE = (0, 1, 2)
    VIDE = 0
    BRIQUE = 1
    PILIER = 2


class Case:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.terrain = t
        self.bomb = 3
        self.explode = 4
        self.player = 5

    def __str__(self):
        # Ces lignes servent uniquement pour les tests (pour que cela soit plus visuel,je l'accorde ça sert à rien)
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0:
            return '  '
        elif self.terrain == 2:
            return '██'
        """return self.terrain"""

    def explode(self):
        if self.terrain == Terrain.brique:
            self.terrain = Terrain.vide
        elif self.player != None:
            self.player.dead = True
        self.bomb = None


a = Grille(13, 11)
a._remplir()
b = a._affichage()
for i in range(len(a.cases)):
    print(b[i])
