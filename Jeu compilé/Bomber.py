from Bomb import Bomb
import pyxel


class Bomber:
    def __init__(self, name, x, y, grille):
        self.grille = grille

        self.x = x
        self.y = y
        self.username = name
        self.dead = False
        self.cool_down = 0  # temps avant de pouvoir poser une bombe
        self.grille.cases[y][x].player = self

        self.slow = 0  # nombre de frames avant le prochain deplacement possible

    def dropbomb(self):
        """pose une bombe, si possible, sous ses pied"""
        if self.cool_down == 0 and self.grille.cases[self.y][self.x].bomb is None:
            bombb = Bomb(self.x, self.y)
            self.grille.cases[self.y][self.x].bomb = bombb
            self.cool_down += 60
            self.grille.all_bombs.append(bombb)

    def goto(self, x, y):
        """deplace le joueur aux coordonnées x,y"""
        self.x = x
        self.y = y
        self.grille.cases[y][x].player = self

    def gauche(self):
        """deplace le joueur vers la gauche si possible"""
        x = self.x - 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def droite(self):
        """deplace le joueur vers la droite si possible"""
        x = self.x + 1
        y = self.y
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def haut(self):
        """deplace le joueur vers le haut si possible"""
        x = self.x
        y = self.y - 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def bas(self):
        """deplace le joueur vers le bas si possible"""
        x = self.x
        y = self.y + 1
        if self.grille.cases[y][x].est_libre():
            self.grille.cases[self.y][self.x].player = None
            self.goto(x, y)

    def deplacement(self, h, b, d, g):
        """gère les deplacements, si une des touche en argument est pressée"""
        if self.slow == 0:
            if pyxel.btn(h):
                self.haut()
                self.slow = 5
            elif pyxel.btn(b):
                self.bas()
                self.slow = 5
            elif pyxel.btn(d):
                self.droite()
                self.slow = 5
            elif pyxel.btn(g):
                self.gauche()
                self.slow = 5

    def update_slow(self):
        """permet le ralentissement des déplacements, sinon instantanés"""
        if self.slow > 0:
            self.slow -= 1