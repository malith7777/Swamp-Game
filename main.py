import pygame
import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import colors as clr

import modules.createObjects as co
from modules.algae import Algae
from modules.duck import Duck
from modules.newt import Newt
from modules.shrimp import Shrimp
from modules.commonFunctions import makeAnimalObjs
from modules.commonFunctions import findCollisions
from modules.commonFunctions import removeDeadAnimals


noOfDucks = int(input("Enter number of ducks (2-4): "))
while (noOfDucks > 4) or (noOfDucks < 2):
    noOfDucks = int(input("Please enter number between 2 and 4: "))

noOfNewts = int(input("Enter number of newts (3-5): "))
while (noOfNewts > 5) or (noOfNewts < 3):
    noOfNewts = int(input("Please enter number between 3 and 5: "))

noOfShrimps = int(input("Enter number of shrimps (4-5): "))
while (noOfShrimps > 5) or (noOfShrimps < 4):
    noOfShrimps = int(input("Please enter number between 4 and 5: "))

noOfAlgae = 5

duckMaxPoints = 70
newtMaxPoints = 90
shrimpMaxPoints = 110


pygame.init() # Initialize PyGame

screen = pygame.display.set_mode((1400, 700)) # Create the Screen

pygame.display.set_caption("Swamp Of Life") # Title


animals = [] # Animals

for i in range(noOfDucks):
    obj = co.createDuck()
    animals.append(Duck(obj))

for i in range(noOfShrimps):
    obj = co.createShrimp()
    animals.append(Shrimp(obj))

for i in range(noOfNewts):
    obj = co.createNewt()
    animals.append(Newt(obj))

for i in range(noOfAlgae):
    obj = co.createAlgae()
    animals.append(Algae(obj))


isRunning = True

while isRunning:
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(0, 0, 1400, 525))
    pygame.draw.rect(screen, (139,69,19), pygame.Rect(0, 525, 1400, 525))
    makeAnimalObjs(animals)
    for animal in animals:
        screen.blit(animal.sizeObj, (animal.positionX, animal.positionY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    for animal in animals:
        if animal.alive:
            if not isinstance(animal, Algae):
                animal.move()

    collisions = findCollisions(animals)
    for collision in collisions:
        animal1 = collision[0]
        animal2 = collision[1]
        # If both animals are ducks then a duck is born
        if isinstance(animal1, Duck) and isinstance(animal2, Duck):
            animal1.reproduce()
            animal2.reproduce()
            co.createDuck()
        elif isinstance(animal1, Newt) and isinstance(animal2, Newt):
            animal1.reproduce()
            animal2.reproduce()
            co.createNewt()
        elif isinstance(animal1, Shrimp) and isinstance(animal2, Shrimp):
            animal1.reproduce()
            animal2.reproduce()
            co.createShrimp()
        else:
            if not isinstance(animal1, Algae) and not animal1.eat(animal2):
                if not isinstance(animal2, Algae):
                    animal2.eat(animal1)
    removeDeadAnimals(animals)
    pygame.display.update()
