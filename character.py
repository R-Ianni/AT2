import pygame
from active_entity import ActiveEntity
from pygame.locals import *
from assets import GAME_ASSETS


class Character(ActiveEntity):
    """
    Class representing a character sprite

    Attributes:
        MAX_LEVEL (int): Maximum level of character
        level (int): Current level of character
        experience_points (int): Experience point stat
        skills (list: Skills): List of skills the character has 
        items (list: Items) List of items the character has 
        gold (int): Amount of gold character has 

    Constructor: (surf, name, attack, defence, level, max_health, hit_points, weapon, is_alive, xcoord, ycoord, experience_points, skills, items, gold)

    Methods:
        gainExperience(self, experience): Increases experience, and if possible levels up.
        updateStats(self): Updates attack, defence based on level.
        calcRequiredExperience(self): Calculates total required experience for the next level.
        takeDamage(self, damage): Changes hitpoints according to defence and damage.
        TODO updatePosition(self, pressed_keys):
        TODO getInfo
    """
    
    # Attributes
    MAX_LEVEL = 50
    __level = None
    __experience_points = None
    __skills = None
    __items = None
    __gold = None

    # Constructor
    def __init__(self, surf, image, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord, level, experience_points, skills, items, gold, healthbar):
        super().__init__(surf, image, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord, healthbar) 
        self.setLevel(level)
        self.setExperiencePoints(experience_points)
        self.setSkills(skills)
        self.setItems(items)
        self.setGold(gold)

    # Getters
    def getLevel(self):
        return self.__level
    def getExperiencePoints(self):
        return self.__experience_points
    def getSkills(self):
        return self.__skills
    def getItems(self):
        return self.__items
    def getGold(self):
        return self.__gold

    # Setters
    def setLevel(self, level):
        self.__level = level
    def setExperiencePoints(self, experience_points):
        self.__experience_points = experience_points
    def setSkills(self, skills):
        self.__skills = skills
    def setItems(self, items):
        self.__items = items
    def setGold(self, gold):
        self.__gold = gold


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
        original_attack = self.getAttack()
        original_defence = self.getDefence()
        self.setAttack(25 + 2 * self.getLevel())
        self.setDefence(25 + 2 * self.getLevel())
        return (self.getAttack() - original_attack, self.getDefence() - original_defence) # returns (gain in attack, gain in defence)

    def calcRequiredExperience(self):
        """
        Calculates total required experience to get to next level
        """ 
        return int(100 * (1.5 ** (self.getLevel()))) # Current formula TODO change: 100 * 1.5^level.

    def getInfo(self):
        """
        Returns character info
        """
        # TODO maybe this can just be generalised??? idk it's only useful for saving so do it later.