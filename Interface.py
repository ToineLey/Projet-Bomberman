import pyxel
from Bomber import Bomber
from Grille import Grille

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
        self.fin_de_partie = False

    def update(self):
        self.player1.deplacement(pyxel.KEY_Z, pyxel.KEY_S, pyxel.KEY_D, pyxel.KEY_Q)
        self.player2.deplacement(pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_RIGHT, pyxel.KEY_LEFT)

        self.player1.dropbomb(pyxel.KEY_E)
        self.player2.dropbomb(pyxel.KEY_1)

        self.grille.manage_bombs()

        self.fin_de_partie = self.player1.dead == True or self.player2.dead == True
           

    def draw(self):
        if self.fin_de_partie == True:
            pyxel.cls(6)
            for h in range(len(self.grille.cases)):
                for l in range(len(self.grille.cases[h-1])):
                    casee = self.grille.cases[h][l]
                    print(casee.terrain)
                    if casee.terrain == 1:
                        pyxel.blt(l*LARG,h*LARG,0,16,0,LARG,LARG)
                    elif casee.terrain == 2:
                        pyxel.blt(l*LARG,h*LARG,0,0,0,LARG,LARG)
                    elif casee.player == self.player1:
                        pyxel.blt(l*LARG,h*LARG,1,0,0,LARG,LARG)
                    elif casee.player == self.player2:
                        pyxel.blt(l*LARG,h*LARG,1,16,0,LARG,LARG)
        else:
            pyxel.text(50, 64, 'GAME OVER', 7)

Jeu()