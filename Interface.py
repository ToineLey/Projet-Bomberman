import pyxel
from Jules import *
from Toine import *


LARG=16

class Jeu:
    def __init__(self):
        pyxel.init(208, 176)
        pyxel.load("resources.pyxres")
        self.fin_de_partie = False
        self.grille = Grille(13, 11)
        self.grille._remplir()
        self.player1 = Bomber('player1', 0, 0, self.grille)
        self.player2 = Bomber('player2', -1, 0, self.grille)
        pyxel.run(self.update,self.draw)

    def update(self):
        if self.fin_de_partie == False:
            if pyxel.btn(pyxel.KEY_Z):
                self.player1.haut()
            elif pyxel.btn(pyxel.KEY_D):
                self.player1.droite()
            elif pyxel.btn(pyxel.KEY_Q):
                self.player1.gauche()
            elif pyxel.btn(pyxel.KEY_S):
                self.player1.bas()
            if pyxel.btn(pyxel.KEY_UP):
                self.player2.haut()
            elif pyxel.btn(pyxel.KEY_RIGHT):
                self.player2.droite()
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.player2.gauche()
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.player2.bas()
        
            if pyxel.btn(pyxel.KEY_E):
                self.player1.dropbomb()
            if pyxel.btn(pyxel.KEY_1):
                self.player2.dropbomb()
            
            self.grille.manage_bombs()
            self.draw()

            self.fin_de_partie = self.player1.dead == True or self.player2.dead == True

        else:
            pyxel.show()
           

    def draw(self):
        pyxel.cls(0)
        for h in range(len(self.grille.cases)):
            for l in range(len(self.grille.cases[h-1])):
                casee = self.grille.cases[h][l]
                if casee.terrain == 1:
                    pyxel.blt(l*LARG,h*LARG,0,32,0,LARG,LARG)
                elif casee.terrain == 2:
                    pyxel.blt(l*LARG,h*LARG,0,0,0,LARG,LARG)
                elif casee.player == self.player1:
                    pyxel.blt(l*LARG,h*LARG,1,0,0,LARG,LARG)
                elif casee.player == self.player2:
                    pyxel.blt(l*LARG,h*LARG,1,32,0,LARG,LARG)


Jeu()
