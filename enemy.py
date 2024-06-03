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
    
    """
# Attributes
    __movement_pattern = None

