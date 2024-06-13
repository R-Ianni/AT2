import pygame
import random
from file_id_interpreter import FileIdInterpreter
from active_entity import ActiveEntity
from assets import GAME_ASSETS
from healthbar import Healthbar
from weapon import Weapon

class Enemy(ActiveEntity):
    """
    Class representing an enemy sprite

    Attributes:
        movement_pattern (str): Represents the algorithm to be used for 
        xp_yield (int): Represents how much xp is earned through defeating enemy
        gold_yield (int): Represents how much gold is earned through defeating enemy
    
    Constructor: (surf, enemy_id, xcoord, ycoord)
    
    Methods:
        calcMovement(self, user_position): Returns a tuple (xcoord, ycoord) representing the square enemy will move to.
        #TODO
        getInfo(self): Returns info of enemy
    """

    # Attributes
    __movement_pattern = None
    __xp_yield = None
    __gold_yield = None

    # Constructor
    def __init__(self, enemy_id, xcoord, ycoord):
        # Getting and unpacking file info
        file_interpreter = FileIdInterpreter('gameinfostorage/enemy_id.txt', enemy_id)
        attribute_list = file_interpreter.interpretFileInfo() # [surf, name, attack, defence, health, weapon, movement_pattern, xp_yield, gold_yield]
        surf, name, attack, defence, health, weapon_id, movement_pattern, xp_yield, gold_yield = attribute_list # unpacks attribute_list
        weapon = Weapon(weapon_id, xcoord, ycoord) # creates weapon object enemy is wielding
        healthbar = Healthbar(pygame.Surface((1,1)), health, health, xcoord, ycoord) # creates healthbar object attached to enemy
    
        # Initialising enemy object. Note that health variable is used to set both max_health and hit_points.
        super().__init__(pygame.Surface((64, 64)), # enemy surface
                         pygame.image.load(GAME_ASSETS[surf]), # enemy image
                         name, attack, defence, health, health, weapon, True, xcoord, ycoord, healthbar)
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