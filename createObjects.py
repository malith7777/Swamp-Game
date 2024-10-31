import pygame
import math

from modules.algae import Algae
from modules.duck import Duck
from modules.newt import Newt
from modules.shrimp import Shrimp

algaeImg = "algae.png"
duckImg = "duck.png"
newtImg = "newt.png"
shrimpImg = "shrimp.png"




def createDuck():
    obj = pygame.image.load(duckImg)
    return obj


def createShrimp():
    obj = pygame.image.load(shrimpImg)
    return obj


def createNewt():
    obj = pygame.image.load(newtImg)
    return obj


def createAlgae():
    obj = pygame.image.load(algaeImg)
    return obj

