class Bomber:
    def __init__(self, name, x, y, grille):
        self.x = x
        self.y = y
        self.username = name
        self.dead = False
        self.grille = grille
        self.cool_down = 100

    def dropbomb(self):
        if self.cool_down == 0 and self.grille.cases[self.x][self.y].bomb == False:
            Bomb(self.x, self.y)
            self.grille.cases[self.x][self.y].bomb = True
            cool_down = 100

    def goto(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        x = self.x - 1
        y = self.y
        try:
            if self.grille.cases[x][y].terrain == 0:
                self.goto(x,y)
        except:
            pass

    def droite(self):
        x = self.x + 1
        y = self.y
        try:
            if self.grille.cases[x][y].terrain == 0:
                self.goto(x,y)
        except:
            pass

    def haut(self):
        x = self.x
        y = self.y - 1
        try:
            if self.grille.cases[x][y].terrain == 0:
                self.goto(x,y)
        except:
            pass

    def bas(self):
        x = self.x
        y = self.y + 1
        try:
            if self.grille.cases[x][y].terrain == 0:
                self.goto(x,y)
        except:
            pass


class Bomb:
    def __init__(self, x, y):
        portee = 4
        self.x = x
        self.y = y
        self.timer = 100