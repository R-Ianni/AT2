import pygame
import random
from entity import Entity
from assets import GAME_ASSETS
from healthbar import Healthbar
from weapon import Weapon

class Enemy(Entity):
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

    # Constructor surf, name, attack, defence, hit_points, max_health, weapon, is_alive, xcoord, ycoord
    def __init__(self, enemy_id, xcoord, ycoord):
        # Interpreting file with enemy_id to get enemy_info
        with open('gameinfostorage/enemy_id.txt', 'r') as enemy_file:
                str_to_find = '!!' + enemy_id # !!{ID} marker
                file_lines = enemy_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains enemy id
                        enemy_info = [i for i in line.split('~')[1].split('/')] # Enemy information split into a list: [surf, name, attack, defence, health, weapon, movement_pattern, xp_yield, gold_yield]
                        break
        
        try: # error handling if enemy_info does not exist
            bool(enemy_info)
        except:
            raise Exception(f"No enemy with ID {enemy_id} found, or enemy file info corrupted")

        surf, name, attack, defence, health, weapon_id, movement_pattern, xp_yield, gold_yield = enemy_info # unpacks all enemy information
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