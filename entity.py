import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    """
    Generalised abstract class that represents a character or an enemy
    Attributes:
        surf (pygame.image): Pygame surface image for the entity
        rect (pygame.Rect): Rectangle representing entity surface position
        name (str): Name of character
        attack (int): Attack stat
        defence (int): Defence stat
        hit_points (int): Current hit points stat
        max_health (int): Maximum hit points stat
        weapon (Weapon): Currently held weapon
        is_alive (bool): Whether entity's is alive: hitpoints above 0 or not
        xcoord (int): X coordinate of entity in world
        ycoord (int): Y coordinate of entity in world
    
    Constructor: (surf, name, attack, defence, hit_points, max_health, weapon, xcoord, ycoord)

    Methods:
        getInfo(self) abstractmethod: Returns the info of entity for saving. TODO might not even be needed with pickling.
        takeDamage(self, amount): Changes hitpoints according to defence and damage.

    """


    # Attributes
    __surf = None
    __rect = None
    __name = None
    __attack = None
    __defence = None
    __hit_points = None
    __max_health = None
    __weapon = None
    __is_alive = None
    __xcoord = None
    __ycoord = None

    # Constructor
    def __init__(self, surf, name, attack, defence, hit_points, max_health, weapon, is_alive, xcoord, ycoord):
        self.setSurf(surf)
        self.setRect(self.getSurf().get_rect())
        self.setName(name)
        self.setAttack(attack)
        self.setDefence(defence)
        self.setHitPoints(hit_points)
        self.setMaxHealth(max_health)
        self.setWeapon(weapon)
        self.setIsAlive(is_alive)
        self.setXcoord(xcoord)
        self.setYcoord(ycoord)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getAttack(self):
        return self.__attack
    def getDefence(self):
        return self.__defence
    def getHitPoints(self):
        return self.__hit_points
    def getMaxHealth(self):
        return self.__max_health
    def getWeapon(self):
        return self.__weapon
    def getIsAlive(self):
        return self.__is_alive
    def getXcoord(self):
        return self.__xcoord
    def getYcoord(self):
        return self.__ycoord

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setAttack(self, attack):
        self.__attack = attack
    def setDefence(self, defence):
        if defence < 0:
            self.__defence = 0
        else:
            self.__defence = defence
    def setHitPoints(self, hit_points):
        max_health = self.getMaxHealth() 
        if hit_points > max_health: # ensures 0 <= hit_points <= max_health
            self.__hit_points = max_health
        elif hit_points < max_health:
            self.__hit_points = 0
            self.setIsAlive(False)
        else:
            self.__hit_points = hit_points
    def setMaxHealth(self, max_health):
        if max_health <= 0: # makes sure max_health > 0
            self.setMaxHealth(1)
        else:
            self.__max_health = max_health
    def setWeapon(self, weapon):
        self.__weapon = weapon
    def setIsAlive(self, is_alive):
        self.__is_alive = is_alive
    def setXcoord(self, xcoord):
        self.__xcoord = xcoord
    def setYcoord(self, ycoord):
        self.__ycoord = ycoord


    # Methods

    @abstractmethod
    def getInfo(self):
        pass

    def takeDamage(self, amount): # amount = raw damage
        """
        Calculate the actual damage taken, taking into account the entity's defence.
        Then subtract from entity's hitpoint.
        """
        actual_damage = max(0, amount - self.defence) # TODO change formula
        self.setHitPoints(self.getHitPoints() - actual_damage)
        if self.getHitPoints() <= 0:
            self.setIsAlive(False)
            print(f"{self.getName()} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.getName()} takes {actual_damage} damage. Remaining hit points: {self.getHitPoints()}/{self.getMaxHealth()}")