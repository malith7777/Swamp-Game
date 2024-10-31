import random
from modules.newt import Newt
from modules.shrimp import Shrimp

duckMaxPoints = 70
reproducePointThreshold = 20


class Duck:
    sizeObj = None
    def __init__(self, imageObj):
        self.points = 0
        self.positionX = random.randint(50, 1350)
        self.positionY = random.randint(50, 650)
        self.imageObj = imageObj
        self.speed = 0.1
        self.alive = True
        self.size = 80
        self.sizeObj = None

    def __dead(self):
        self.alive = False

    def __increasePoints(self, points):
        self.points += points
        self.size += 10
        if self.points >= duckMaxPoints:
            self.__dead()
        else:
            self.speed += 0.1

    def eat(self, food):
        if isinstance(food, Newt):
            self.points += 20
            self.__increasePoints(20)
            food.eaten()
            return True
        elif isinstance(food, Shrimp):
            self.__increasePoints(15)
            food.eaten()
            return True
        return False

    def canReproduce(self):
        return self.points > reproducePointThreshold

    def reproduce(self):
        self.__increasePoints(25)
        return True

    def move(self):
        self.positionX += self.speed
        self.positionY += self.speed
        if self.positionX <= 0:
            self.positionX = random.randint(0,1350)
        elif self.positionX >= 1350:
            self.positionX = random.randint(0,1350)

        if self.positionY <= 0:
            self.positionY = random.randint(0,650)
        elif self.positionY >= 650:
            self.positionY = random.randint(0,650)

