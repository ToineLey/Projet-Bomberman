import pyxel
from Jules import *
from Toine import *


TAILLE=50

class Jeu:
    def __init__(self):
        pyxel.init(104, 88)
        pyxel.load("resources.pyxres")
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
                if casee.terrain == 1:
                    pyxel.blt(l*8,h*8,0,16,0,8,8)
                elif casee.terrain == 2:
                    pyxel.blt(l*8,h*8,0,0,0,8,8)


Jeu()
