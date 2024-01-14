import pyxel
from Bomber import Bomber
from Grille import Grille

LARG = 16


class Jeu:
    def __init__(self):
        pyxel.init(240, 208)
        pyxel.load("resources.pyxres")
        self.fin_de_partie = 0
        self.grille = Grille(13, 11)
        self.grille._remplir()
        self.player1 = Bomber('player1', 1, 1, self.grille)
        self.player2 = Bomber('player2', -2, 1, self.grille)
        """b = self.grille._affichage()
        for i in range(len(self.grille.cases)):
            print(b[i])"""
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Z):
            self.player1.haut()
        elif pyxel.btn(pyxel.KEY_S):
            self.player1.bas()
        elif pyxel.btn(pyxel.KEY_D):
            self.player1.droite()
        elif pyxel.btn(pyxel.KEY_Q):
            self.player1.gauche()

        if pyxel.btn(pyxel.KEY_UP):
            self.player2.haut()
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.player2.bas()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.player2.droite()
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.player2.gauche()
        """self.player1.deplacement(pyxel.KEY_Z, pyxel.KEY_S, pyxel.KEY_D, pyxel.KEY_Q)
        self.player2.deplacement(pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_RIGHT, pyxel.KEY_LEFT)"""

        if pyxel.btn(pyxel.KEY_E):
            self.player1.dropbomb()

        if pyxel.btn(pyxel.KEY_KP_1):
            self.player2.dropbomb()

        self.grille.manage_bombs()

        """self.fin_de_partie = self.player1.dead == True or self.player2.dead == True"""

        if self.player1.dead == True:
            self.fin_de_partie = 2

        if self.player2.dead == True:
            self.fin_de_partie = 1
        
        if self.player2.dead == True and self.player1.dead == True:
            self.fin_de_partie = 3

        if self.player1.cool_down > 0:
            self.player1.cool_down -= 1

        if self.player2.cool_down > 0:
            self.player2.cool_down -= 1

    def draw(self):
        if self.fin_de_partie == 0:
            pyxel.cls(6)
            for h in range(len(self.grille.cases)):
                for l in range(len(self.grille.cases[h-1])):
                    casee = self.grille.cases[h][l]
                    if casee.bomb is not None:
                        print(casee.bomb.timer)
                    if casee.explosion != 0:
                        pyxel.blt(l*LARG, h*LARG, 0, 0, 16, LARG, LARG)
                    if casee.bomb is not None:
                        pyxel.blt(l*LARG, h*LARG, 0, 48, 0, LARG, LARG)
                    if casee.terrain == 1:
                        pyxel.blt(l*LARG, h*LARG, 0, 16, 0, LARG, LARG)
                    elif casee.terrain == 2:
                        pyxel.blt(l*LARG, h*LARG, 0, 0, 0, LARG, LARG)
                    elif casee.player == self.player1:
                        pyxel.blt(l*LARG, h*LARG, 1, 0, 0, LARG, LARG)
                    elif casee.player == self.player2:
                        pyxel.blt(l*LARG, h*LARG, 1, 16, 0, LARG, LARG)
        else:
            pyxel.cls(0)
            if self.fin_de_partie == 2:
                message = 'PLAYER 2 WINS'
            elif self.fin_de_partie == 1:
                message = 'PLAYER 1 WINS'
            else:
                message = "  GAME OVER  "

            pyxel.text(120-25, 104-5, message, 7)


Jeu()
