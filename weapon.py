import pygame 

class Weapon:
    """
    A class representing a weapon.

    Attributes:
        surf (pygame.Surface): The weapon surface.
        rect (pygame.Rect): The weapon surface's rectangle
        name (str): The name of the weapon
        attacks (list): The list of attacks the weapon has

    Methods:
        __init__(self, window): Initializes the Weapon object.
    """
    
    # Attributes
    __surf = None
    __rect = None
    __name = None
    __attacks = None

    # Constructor
    def __init__(self, surf, rect, name, attacks):
        self.setSurf(surf)
        self.setRect(rect)
        self.setName(name)
        self.setAttacks(attacks)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getAttacks(self):
        return self.__attacks

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setAttacks(self, attacks):
        self.__attacks = attacks