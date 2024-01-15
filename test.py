from Grille import Grille
from Case import Case
from Bomber import Bomber
import pyxel

# programme de test pour voir si la grille fonctionne correctement

a = Grille(13, 11)
a.remplir_niveau_1()
b = a._affichage()
player1 = Bomber('player1', 1, 1, a)
player2 = Bomber('player2', -2, 1, a)
for i in range(len(a.cases)):
    print(b[i])

# programme de test pour voir si notre gestion des touches était juste


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = pyxel.width//2
        self.y = pyxel.height//2
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT) == True:
            self.x = (self.x + 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_DOWN) == True:
            self.y = (self.y + 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_UP) == True:
            self.y = (self.y - 1) % pyxel.height
        if pyxel.btn(pyxel.KEY_LEFT) == True:
            self.x = (self.x - 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.circ(self.x, self.y, 8, 9)


App()


#   essai d'ajout d'une classe fille qui définiele str de Case 

class Case_test(Case):
    def __str__(self):
        if self.terrain == 1:
            return '▒▒'
        elif self.terrain == 0 and self.player is None:
            return '  '
        elif self.terrain == 2:
            return '██'
        elif self.bomb is not None:
            return '!!'
        elif self.player is not None:
            return '()'
        elif self.explosion != 0:
            return '**'
