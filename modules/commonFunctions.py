import pygame
import math
import modules.createObjects as co
from modules.algae import Algae

ct = 50 # Collision Threshold

def makeAnimalObjs(animals):
    for animal in animals:
        obj = pygame.transform.scale(animal.imageObj, (animal.size, animal.size))
        animal.sizeObj = obj


def findCollisions(animals):
    try:
        collisionPairs = []
        for i in range(len(animals)):
            animal1 = animals[i]
            for j in range(i + 1, len(animals)):
                animal2 = animals[j]
                xDistance = abs(animal1.positionX - animal2.positionX)
                yDistance = abs(animal1.positionY - animal2.positionY)
                distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
                if distance <= ct:
                    collisionPairs.append([animal1, animal2])
        return collisionPairs
    except:
        pass


def removeDeadAnimals(animals):
    #global animals
    for i in range(len(animals)):
        if not animals[i].alive:
            animals[i] = None
    i = 0
    while True:
        if animals[i] is None:
            del animals[i]
        else:
            i += 1
        if i >= len(animals):
            break
    algaeCount = 0
    for animal in animals:
        if isinstance(animal, Algae):
            algaeCount += 1
    if not algaeCount == 3:
        while algaeCount < 3:
            co.createAlgae()
            algaeCount += 1