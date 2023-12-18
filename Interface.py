import pyxel
from Jules import *
from Backend import *

class Jeu:
    def __init__(self):
        grille = Grille(x, y)
        bomber1 = Bomber(input("Entrez votre nom, joueur 1"), x, y, grille)
        bomber2 = Bomber(input("Entrez votre nom, joueur 2"), x, y, grille)

    def update(self):
        pass

    def draw(self):
        pass