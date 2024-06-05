import pygame
import random
from entity import Entity

class Enemy(Entity):
    """
    Class representing an enemy

    Attributes:
        movement_pattern (str): Represents the algorithm to be used for 
        xp_yield (int): Represents how much xp is earned through defeating enemy
        gold_yield (int): Represents how much gold is earned through defeating enemy
    
    Constructor: (surf, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord, movement_pattern, xp_yield, gold_yield)
    
    Methods:
    calcMovement(self, user_position): Returns a tuple (xcoord, ycoord) representing the square enemy will move to.

    getInfo(self): Returns info of enemy
    """

    # Attributes
    __movement_pattern = None
    __xp_yield = None
    __gold_yield = None

    # Constructor surf, name, attack, defence, hit_points, max_health, weapon, is_alive, xcoord, ycoord
    def __init__(self, surf, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord, movement_pattern, xp_yield, gold_yield):
        super().__init__(surf, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord)
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

    # Methods
    def getInfo(self):
        pass