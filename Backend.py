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

    """
    def update_bomb(self):
        "compte a rebour des bombes"
        for bomb in all_bombs:
            bomb.rebour()
            if bomb.timer == 0:
                exploding_bomb.append(bomb)
        
    def update_explosions(self, x, y):
        "met a jour les cases en cours d'explosion autour de celle au coordonees x,y"

        case = self.get(x, y)
        i = 1

        ## Partie qui suit à optimiser ##

        while i <= Bomb.portee:
            current_case = self.get(x, y+i)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x, y-i)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x+i, y)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
        i = 1
        while i <= Bomb.portee:
            current_case = self.get(x-i, y)
            current_case.explode = True
            if current_case.bomb != None:
                exploding_bomb.append(current_case.bomb)
                break
            elif current_case.terrain == Terrain.pilier:
                break
                
    def bombs_explosion(self):
        "fait exploser les bombes"
        for bomb in self.exploding_bombs:
            self.update_explosions(bomb.x, bomb.y)
        self.explosions()
            
    def explosions(self):
        "explosions des cases"
        for case in get_explosions():
            case.explode()
    """


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

    """
    def explode(self):
        if self.terrain == Terrain.brique:
            self.terrain = Terrain.vide
        elif self.player != None:
            self.player.dead = True
        self.bomb = None
    """
    

a=Grille(13,11)
a._remplir()
print(a.cases)
