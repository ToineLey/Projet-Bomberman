from Grille import Grille
from Case import Case
import pyxel
"""a = Grille(13, 11)
a._remplir()
b = a._affichage()
for i in range(len(a.cases)):
    print(b[i])"""



class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT)== True:
            self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()




class Case_test(Case):
    def __str__(self):
        # Ces lignes servent uniquement pour les tests (pour que cela soit plus visuel,je l'accorde ça sert à rien)
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0 and self.player is None:
            return '  '
        elif self.terrain == 2:
            return '██'
        elif self.player is not None:
            return '()'