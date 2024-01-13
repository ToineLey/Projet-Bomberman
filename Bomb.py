class Bomb:
    portee = 4
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 100

    def rebour(self):
        self.timer -= 1