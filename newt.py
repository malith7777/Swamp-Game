import random
from modules.algae import Algae
from modules.shrimp import Shrimp

newtMaxPoints = 90
reproducePointThreshold = 20

class Newt:
    sizeObj = None
    def __init__(self,imageObj):
        self.points = 0
        self.positionX = random.randint(50, 1350)
        self.positionY = random.randint(50, 650)
        self.imageObj = imageObj
        self.speed = 0.1
        self.alive = True
        self.size = 70
        self.sizeObj = None

    def __dead(self):
        self.alive = False

    def __increasePoints(self,points):
        self.size += 10
        self.points += points
        if self.points >= newtMaxPoints:
            self.__dead()
        else:
            self.speed += 0.1

    def eat(self,food):
        if isinstance(food,Shrimp):
            self.__increasePoints(15)
            food.eaten()
            return True
        elif isinstance(food,Algae):
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
        return True


    def move(self):
        self.positionY += self.speed
        if self.positionY <= 0:
            self.positionY = random.randint(0,650)
        elif self.positionY >= 650:
            self.positionY = random.randint(0,650)
