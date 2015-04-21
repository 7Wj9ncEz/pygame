import pygame, sys, random
from pygame.locals import *

class Food:

    def __init__(self, newFoodCounter, foodScore, window):
        self.foodCounter = 0
        self.foodSize = 20
        self.newFoodCounter = newFoodCounter
        self.foodScore = foodScore
        self.rectangle = pygame.Rect(random.randint(0, window[0]-self.foodSize), random.randint(0, window[1] - self.foodSize), self.foodSize, self.foodSize)

class GreenFood(Food):

    def __init__(self, window):
        Food.__init__(self, 40, 1, window)

class RedFood(Food):

    def __init__(self, window):
        Food.__init__(self, 100, 2, window)

class BlueFood(Food):

    def __init__(self, window):
        Food.__init__(self, 200, 5, window)

class Poison(Food):

    def __init__(self, window):
        Food.__init__(self, 300, -5, window)


