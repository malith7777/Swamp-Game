import random


class Algae:
    def __init__(self,imageObj):
        self.points = 0
        self.positionX = random.randint(30, 1300)
        self.positionY = random.randint(30, 400)
        self.imageObj = imageObj
        self.alive = True
        self.size = 50

    def eaten(self):
        self.alive = False
