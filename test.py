from Toine import *


a = Grille(13, 11)
a._remplir()
b = a._affichage()
for i in range(len(a.cases)):
    print(b[i])