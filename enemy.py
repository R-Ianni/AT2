import pygame
import random
from entity import Entity

class Enemy(Entity):
    """
    Class representing an enemy

    Attributes:
        movement_pattern (str):
        xp_yield (int):
        gold_yield (int):
    
    Constructor: (surf, name, attack, defence, hit_points, max_health, weapon, xcoord, ycoord, movement_pattern, xp_yield, gold_yield)
    
    Methods:


    getInfo(self): Returns info
    """

    # Attributes
    __movement_pattern = None
    __xp_yield = None
    __gold_yield = None

    # Constructor
    def __init__(self, surf, name, attack, defence, hit_points, max_health, weapon, xcoord, ycoord, movement_pattern, xp_yield, gold_yield):
        super().__init(surf, name, attack, defence, hit_points, max_health, weapon, xcoord, ycoord)
        self.setMovementPattern(movement_pattern)
        self.setXpYield(xp_yield)
        self.setGoldYield(gold_yield)

    # Getters
    def getMovementPattern(self):
        return self.__movement_pattern
    def getXpYield(self):
        return self.__xp_yield
    def getGoldYield(self):
        return self.__gold_yield

    # Setters
    def setMovementPattern(self, movement_pattern):
        self.__movement_pattern = movement_pattern
    def setXpYield(self, xp_yield):
        self.__xp_yield = xp_yield
    def setGoldYield(self, gold_yield):
        self.__gold_yield = gold_yield

