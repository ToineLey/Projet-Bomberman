class Grille:
    def __init__(self, l: int, h: int):
        self.hauteur = h
        self.largeur = l
        self.cases = [[j for j in range(l)] for i in range(h)]
    def _remplir(self):
        def ot():
            return (
                n not in (0,self.largeur-1) and
                a not in (0,self.hauteur-1) and
                a%2!=0 and
                n%2!=0
            )
        def at():
            return (
                a in (0,1) and
                n in (1,self.largeur-2,self.largeur-1)
            )
        for a in range(len(self.cases)):
            for n in self.cases[a]:
                if ot():
                    self.cases[a][n]=Case(a,n,2)
                elif at():
                    self.cases[a][n]=Case(a,n,0)
                else:
                    self.cases[a][n]=Case(a,n,1)


class Case:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.terrain = t
        self.bomb = 3
        self.explode = 4
        self.player = 5
    def __str__(self):
        return self.terrain
    

a=Grille(13,11)
a._remplir()
print(a.cases)
