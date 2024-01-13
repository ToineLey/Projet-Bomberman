from Grille import Grille
from Case import Case

a = Grille(13, 11)
a._remplir()
b = a._affichage()
for i in range(len(a.cases)):
    print(b[i])

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