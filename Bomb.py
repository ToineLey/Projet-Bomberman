class Bomb:
    portee = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 30

    def rebour(self):
        self.timer -= 1
