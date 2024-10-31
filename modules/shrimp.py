import random
from modules.algae import Algae

shrimpMaxPoints = 110
reproducePointThreshold = 20

class Shrimp:
    sizeObj = None
    def __init__(self, imageObj):
        self.points = 0
        self.positionX = random.randint(50, 1350)
        self.positionY = random.randint(50, 475)
        self.imageObj = imageObj
        self.speed = 0.1
        self.alive = True
        self.size = 50
        self.sizeObj = None

    def __dead(self):
        self.alive = False

    def __increasePoints(self,points):
        self.size += 10
        self.points += points
        if self.points >= shrimpMaxPoints:
            self.__dead()
        else:
            self.speed +=0.1


    def eat(self, food):
        if isinstance(food, Algae):
            self.__increasePoints(10)
            food.eaten()
            return True
        return False

    def eaten(self):
        self.alive = False

    def canReproduce(self):
        return self.points > reproducePointThreshold

    def reproduce(self):
        self.__increasePoints(25)

    def move(self):
        self.positionX += self.speed
        if self.positionX <= 0:
            self.positionX = random.randint(0,1350)
        elif self.positionX >= 1350:
            self.positionX = random.randint(0,1350)

