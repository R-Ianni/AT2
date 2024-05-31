import pygame
from pygame.locals import *
from assets import GAME_ASSETS

class Character():
    """
    A class representing a character

    Attributes:
    MAX_LEVEL (int): Maximum level of character
    LVLUP_ATK_INCR (int): Number of points attack increases per level
    LVLUP_DEF_INCR (int): Number of points defence increases per level
    WORLD_SPEED (int): Number of pixels character moves per frame

    surf (pygame.image): Surface for the character
    rect (pygame.Rect): Rectangle representing character surface position
    name (str): Name of character
    attack (int): Attack stat
    defence (int): Defence stat
    movement_points (int): Movement points stat
    level (int): Level stat
    experience points (int): Experience point stat
    hit_points (int): Current hit points stat
    max_health (int): Maximum hit points stat
    weapon (Weapon): Currently held weapon
    is_alive (bool): Whether character's hit points above 0 or not
    skills (list: Skills): List of skills the character has

    Methods:
    gainExperience(self, experience): 
    updateStats(self)
    """
    
    # Attributes
    MAX_LEVEL = 50
    LVLUP_ATK_INCR = 2
    LVLUP_DEF_INCR = 2
    WORLD_SPEED = 5
    __surf = None
    __rect = None
    __name = None
    __attack = None
    __defence = None
    __movement_points = None
    __level = None
    __experience_points = None
    __hit_points = None
    __max_health = None
    __weapon = None
    __is_alive = None
    __skills = None
    
    # TODO add attribute describing board position
    # TODO generalise character, enemy under entity class.

    # Example character:
    # Character(pygame.image.load(GAME_ASSETS['blue_orb'], )

    # Constructor
    def __init__(self, surf, name, attack, defence, movement_points, level, experience_points, hit_points, max_health, weapon, is_alive, skills):
        self.setSurf(surf)
        self.setRect(self.getSurf().get_rect())
        self.setName(name) # replace with name
        self.setAttack(25)
        self.setDefence(25)
        self.setMovementPoints(2)
        self.setLevel(1)
        self.setExperiencePoints(0)
        self.setHitPoints(1000)
        self.setMaxHealth(1000)
        self.setWeapon('fists') # TODO replace with starter weapon / character initialisation screen.
        self.setIsAlive(True)
        self.setSkills(list())

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
    def getMovementPoints(self):
        return self.__movement_points
    def getLevel(self):
        return self.__level
    def getExperiencePoints(self):
        return self.__experience_points
    def getHitPoints(self):
        return self.__hit_points
    def getMaxHealth(self):
        return self.__max_health
    def getWeapon(self):
        return self.__weapon
    def getIsAlive(self):
        return self.__is_alive
    def getSkills(self):
        return self.__skills

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
        self.__defence = defence
    def setMovementPoints(self, movement_points):
        self.__movement_points = movement_points
    def setLevel(self, level):
        self.__level = level
    def setExperiencePoints(self, experience_points):
        self.__experience_points = experience_points
    def setHitPoints(self, hit_points):
        self.__hit_points = hit_points
    def setMaxHealth(self, max_health):
        self.__max_health = max_health
    def setWeapon(self, weapon):
        self.__weapon = weapon
    def setIsAlive(self, is_alive):
        self.__is_alive = is_alive
    def setSkills(self, skills):
        self.__skills = skills

    # Methods
    def gainExperience(self, experience):
        """
        Increases character's experience, and increases levels accordingly. Subtracts used experience.
        Runs stat increase method based on levels gained.
        """
        self.setExperiencePoints(self.getExperiencePoints() + experience)  # Increase character's experience points
        required_experience = self.calcRequiredExperience() # Calculate experience required for next level

        # Level up character while character has enough experience to level up and is below the level cap.
        while self.getExperiencePoints() >= required_experience and self.getLevel() < self.MAX_LEVEL:
            self.setLevel(self.getLevel() + 1) # Level up the character if sufficient experience.
            self.setExperiencePoints(self.getExperiencePoints() - required_experience) # Decrease character's experience points based on those used.
            required_experience = self.calcRequiredExperience() # Re-calculate experience required for next level

        self.updateStats() # TODO have it also print out stat gains. If stat gains are more than 1, then print.
        print(f"Level up! {self.getName()} is now level {self.getLevel()}.")

    def updateStats(self):
        """
        Updates attack, defence based on level. Formula: 25 + 2 * level
        Returns tuple: (increase in attack, increase in defence)
        """
        self.setAttack(25 + 2 * self.getLevel())
        self.setDefence(25 + 2 * self.getLevel())

    def calcRequiredExperience(self):
        """
        Calculates total required experience to get to next level
        """
        return int(100 * (1.5 ** (self.getLevel())))

    def takeDamage(self, amount): # amount = raw damage
        """
        Calculate the actual damage taken, taking into account the character's defence.
        Then subtract from character's hitpoint.
        """
        actual_damage = max(0, amount - self.defence)
        self.setHitPoints(self.getHitPoints() - actual_damage)
        if self.getHitPoints() <= 0:
            self.setIsAlive(False)
            print(f"{self.getName()} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.getName()} takes {actual_damage} damage. Remaining hit points: {self.getHitPoints()}/{self.getMaxHealth()}")
