from Bomb import Bomb
import pyxel


class Bomber:
    def __init__(self, name, x, y, grille):
        self.grille = grille

        self.x = x
        self.y = y
        self.username = name
        self.dead = False
        self.cool_down = 60
        self.grille.cases[y][x].player = self

        self.slow = 0

    def dropbomb(self):
        "pose d'une bombe si possible"
        if self.cool_down == 0 and self.grille.cases[self.y][self.x].bomb is None:
            bombb = Bomb(self.x, self.y)
            self.grille.cases[self.y][self.x].bomb = bombb
            self.cool_down += 60
            self.grille.all_bombs.append(bombb)

    def goto(self, x, y):
        "deplace le joueur en x,y"
        self.x = x
        self.y = y
        self.grille.cases[y][x].player = self

    def gauche(self):
        "deplacement vers la gauche"
        x = self.x - 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def droite(self):
        "deplacement vers la droite"
        x = self.x + 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def haut(self):
        "deplacement vers le haut"
        x = self.x
        y = self.y - 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def bas(self):
        "deplacement vers le bas"
        x = self.x
        y = self.y + 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def deplacement(self, h, b, d, g):
        if self.slow == 0:
            if pyxel.btn(h):
                self.haut()
            elif pyxel.btn(b):
                self.bas()
            elif pyxel.btn(d):
                self.droite()
            elif pyxel.btn(g):
                self.gauche()
            self.slow = 10

    def update_slow(self):
        if self.slow > 0:
            self.slow -= 1
