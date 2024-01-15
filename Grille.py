from Terrain import Terrain
from Bomb import Bomb
from random import randint
from Case import Case


class Grille:
    def __init__(self, l: int, h: int):
        self.hauteur = h
        self.largeur = l
        self.cases = [[j for j in range(l+2)] for _ in range(h+2)]
        self.exploding_bombs = []
        self.all_bombs = []

    def remplir_niveau_1(self):
        """cette méthode sert à remplir la grille de jeu pour que cela soit le niveau 1"""

        hauteur = self.hauteur+2
        largeur = self.largeur+2

        def espacement_piliers():
            """cette fonction sert à ajouter un espacement entre les piliers"""

            return (
                x not in (1, largeur-2) and
                y not in (1, hauteur-2) and
                y % 2 == 0 and
                x % 2 == 0
            )

        def depart():
            """cette fonction sert à ajouter les zones de départ pour les joueurs"""

            return (
                y in (1, 2) and
                x in (1, 2, largeur-3, largeur-2)
            )

        def contour():
            """cette fonction sert à ajouter le contour de la zone de jeu (c'est pour pas se téléporter de l'autre côté de la grille)"""

            return (
                x in (0, largeur-1) or
                y in (0, hauteur-1)
            )

        # la boucle suivante sert à remplir la grille de jeu

        for y in range(len(self.cases)):
            for x in self.cases[y]:
                alea = randint(1, 100)
                if contour():
                    self.cases[y][x] = Case(y, x, Terrain.PILIER)
                elif espacement_piliers():
                    self.cases[y][x] = Case(y, x, Terrain.PILIER)
                elif depart():
                    self.cases[y][x] = Case(y, x, Terrain.VIDE)
                else:
                    if alea <= 20:
                        self.cases[y][x] = Case(y, x, Terrain.VIDE)
                    else:
                        self.cases[y][x] = Case(y, x, Terrain.BRIQUE)

    def _affichage(self):
        """cette partie n'est utile uniquement dans les tests"""

        t2 = []
        for a in range(len(self.cases)):
            t1 = []
            for el in self.cases[a]:
                t1.append(str(el))
            t2.append(t1)
        return t2

    def get(self, x: int, y: int):
        """ça permet de récupérer la case au coordonnés (x;y)"""

        return self.cases[y][x]

    def get_explosions(self) -> list:
        """ça permet de savoir quelles bombes sont actuellement placés"""

        c = []
        for a in range(len(self.cases)):
            for el in self.cases[a]:
                if el.explosion != 0:
                    c.append(el)
        return c

    def update_bomb(self):
        "compte a rebour des bombes"
        for bomb in self.all_bombs:
            bomb.rebour()
            if bomb.timer == 0:
                self.exploding_bombs.append(bomb)

    def update_explosions(self, x, y):
        "met a jour les cases en cours d'explosion autour de celle au coordonees x,y"

        case = self.get(x, y)
        case.explosion = 15
        i = 1

        while i <= Bomb.portee:
            current_case = self.get(x, y+i)
            current_case.explosion = 15
            if current_case.bomb != None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER:
                break
            i += 1
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y-i)
            current_case.explosion = 15
            if current_case.bomb != None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER:
                break
            i += 1
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x+i, y)
            current_case.explosion = 15
            if current_case.bomb != None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER:
                break
            i += 1
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x-i, y)
            current_case.explosion = 15
            if current_case.bomb != None:
                self.exploding_bombs.append(current_case.bomb)
            elif current_case.terrain == Terrain.PILIER:
                break
            i += 1

    def bombs_explosion(self):
        "fait exploser les bombes"
        for bomb in self.exploding_bombs:
            self.update_explosions(bomb.x, bomb.y)

    def explosions(self):
        "explosions des cases"
        for case in self.get_explosions():
            case.explode()
        for bomb in self.exploding_bombs:
            self.all_bombs.remove(bomb)
        self.exploding_bombs = []

    def manage_bombs(self):
        """gère tout ce qui ce passe au niveau des bombes"""

        self.update_bomb()
        self.bombs_explosion()
        self.explosions()
