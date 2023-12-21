import pyxel
from Jules import *
from Toine import *


TAILLE=50

class Jeu:
    def __init__(self):
        pyxel.init(650, 550)
        self.grille = Grille(13, 11)
        self.grille._remplir()
        pyxel.run(self.update,self.draw)
    def update(self):
        pass
    def draw(self):
        pyxel.cls(0)
        for h in range(len(self.grille.cases)):
            for l in range(len(self.grille.cases[h-1])):
                casee = self.grille.cases[h][l]
                if casee.terrain == 0:
                    col = 0
                elif casee.terrain == 1:
                    col = 9
                else:
                    col = 2
                pyxel.rect(l*TAILLE,h*TAILLE,(l+1)*TAILLE,(h+1)*TAILLE,col)


Jeu()
