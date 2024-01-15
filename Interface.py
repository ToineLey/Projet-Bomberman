import pyxel
from Bomber import Bomber
from Grille import Grille

LARGEUR_SPRITE = 16


class Jeu:
    def __init__(self):
        pyxel.init(240, 208)
        pyxel.load("resources.pyxres")
        self.fin_de_partie = 0
        self.grille = Grille(13, 11)
        self.grille.remplir_niveau_1()
        self.player1 = Bomber('player1', 1, 1, self.grille)
        self.player2 = Bomber('player2', -2, 1, self.grille)
        pyxel.run(self.update, self.draw)


    def update(self):

        # déplacements des joueurs

        self.player1.update_slow()
        self.player2.update_slow()

        self.player1.deplacement(
            pyxel.KEY_Z, pyxel.KEY_S, pyxel.KEY_D, pyxel.KEY_Q)

        self.player2.deplacement(
            pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_RIGHT, pyxel.KEY_LEFT)

        # poses de bombes

        if pyxel.btn(pyxel.KEY_E):
            self.player1.dropbomb()

        if pyxel.btn(pyxel.KEY_KP_1) or pyxel.btn(pyxel.KEY_END):
            self.player2.dropbomb()

        # mise à jour de la grille des bombes

        self.grille.manage_bombs()

        # fonctionnement des cooldown de pose de bombes

        if self.player1.cool_down > 0:
            self.player1.cool_down -= 1

        if self.player2.cool_down > 0:
            self.player2.cool_down -= 1

        # tests de fin de partie

        if self.player1.dead == True:
            self.fin_de_partie = 2

        if self.player2.dead == True:
            self.fin_de_partie = 1

        if self.player2.dead == True and self.player1.dead == True:
            self.fin_de_partie = 3


    def draw(self):
        if self.fin_de_partie == 0:
            pyxel.cls(3)

            # affichage du jeu

            for h in range(len(self.grille.cases)):
                for l in range(len(self.grille.cases[h-1])):
                    casee = self.grille.cases[h][l]
                    if casee.explosion != 0:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  0, 32, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
                    if casee.bomb is not None:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  0, 48, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
                    if casee.terrain == 1:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  0, 16, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
                    elif casee.terrain == 2:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  0, 0, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
                    elif casee.player == self.player1:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  1, 0, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
                    elif casee.player == self.player2:
                        pyxel.blt(l*LARGEUR_SPRITE, h*LARGEUR_SPRITE,
                                  1, 16, 0, LARGEUR_SPRITE, LARGEUR_SPRITE)
        else:

            # affichage de l'écran de fin

            pyxel.cls(0)
            if self.fin_de_partie == 2:
                message = 'PLAYER 2 WINS'
            elif self.fin_de_partie == 1:
                message = 'PLAYER 1 WINS'
            else:
                message = "  GAME OVER  "

            pyxel.text(
                (pyxel.width//2)-25,
                (pyxel.height//2)-5,
                message, 7
            )


Jeu()
