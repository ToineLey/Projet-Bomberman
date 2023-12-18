class Bomber:
    def __init__(self, name, x, y, grille):
        self.x = x
        self.y = y
        self.username = name
        self.dead = False
        self.grille = grille
        self.cool_down = 100

    def dropbomb(self):
        "pose d'une bombe si possible"
        if self.cool_down == 0 and self.grille.cases[self.x][self.y].bomb == False:
            Bomb(self.x, self.y)
            self.grille.cases[self.x][self.y].bomb = True
            cool_down = 100

    def goto(self, x, y):
        "deplace le joueur en x,y"
        self.x = x
        self.y = y

    def gauche(self):
        "deplacement vers la gauche"
        x = self.x - 1
        y = self.y
        if self.grille.cases[x][y]..est_libre():
            self.goto(x,y)

    def droite(self):
        "deplacement vers la droite"
        x = self.x + 1
        y = self.y
        if self.grille.cases[x][y]..est_libre():
            self.goto(x,y)

    def haut(self):
        "deplacement vers le haut"
        x = self.x
        y = self.y - 1
        if self.grille.cases[x][y].est_libre():
            self.goto(x,y)

    def bas(self):
        "deplacement vers le bas"
        x = self.x
        y = self.y + 1
        if self.grille.cases[x][y].est_libre():
            self.goto(x,y)


class Bomb:
    portee = 4
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 100

    def rebour(self):
        self.timer -= 1