from random import randint
from Jules import *


class Grille:
    def __init__(self, l: int, h: int):
        self.hauteur = h
        self.largeur = l
        self.cases = [[j for j in range(l)] for _ in range(h)]
        self.exploding_bombs = []
        self.all_bombs = []

    def _remplir(self):
        def ot():
            return (
                x not in (0, self.largeur-1) and
                y not in (0, self.hauteur-1) and
                y % 2 != 0 and
                x % 2 != 0
            )

        def at():
            return (
                y in (0, 1) and
                x in (0, 1, self.largeur-2, self.largeur-1)
            )
        for y in range(len(self.cases)):
            for x in self.cases[y]:
                alea = randint(1, 100)
                if ot():
                    self.cases[y][x] = Case(y, x, Terrain.PILIER)
                elif at():
                    self.cases[y][x] = Case(y, x, Terrain.VIDE)
                else:
                    if alea <= 20:
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    else:
                        self.cases[y][x] = Case(y, x, Terrain.BRIQUE)

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

    def get_explosion(self):
        c = []
        for a in range(len(self.cases)):
            for el in self.cases[a]:
                if el.explode:
                    c.append(el)

    def update_bomb(self):
        "compte a rebour des bombes"
        for bomb in self.all_bombs:
            bomb.rebour()
            if bomb.timer == 0:
                self.exploding_bomb.append(bomb)

    def update_explosions(self, x, y):
        "met a jour les cases en cours d'explosion autour de celle au coordonees x,y"

        case = self.get(x, y)
        i = 1

        # Partie qui suit à optimiser (jusqu'à la ligne 100)

        while i <= Bomb.portee:
            current_case = self.get(x, y+i)
            current_case.explosion = True
            if current_case.bomb != None:
                self.exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.PILIER:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y-i)
            current_case.explosion = True
            if current_case.bomb != None:
                self.exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.PILIER:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x+i, y)
            current_case.explosion = True
            if current_case.bomb != None:
                self.exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.PILIER:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x-i, y)
            current_case.explosion = True
            if current_case.bomb != None:
                self.exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.PILIER:
                break

    def bombs_explosion(self):
        "fait exploser les bombes"
        for bomb in self.exploding_bombs:
            self.update_explosions(bomb.x, bomb.y)
        self.explosions()

    def explosions(self):
        "explosions des cases"
        for case in self.get_explosions():
            case.explode()
        for bomb in self.expoding_bombs:
            self.all_bombs.remove(bomb)
        self.exploding_bombs = []

    def manage_bombs(self):
        self.update_bomb()
        self.bombs_explosion()
        self.exposions()


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
        self.bomb = False
        self.explosion = False
        self.player = False

    def __str__(self):
        # Ces lignes servent uniquement pour les tests (pour que cela soit plus visuel,je l'accorde ça sert à rien)
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0:
            return '  '
        elif self.terrain == 2:
            return '██'

    def terraininfy(self):
        return self.terrain

    def explode(self):
        if self.terrain == Terrain.BRIQUE:
            self.terrain = Terrain.VIDE
        elif self.player != None:
            self.player.dead = True
        self.bomb = None



