from abc import ABC, abstractmethod
import pygame
# TODO Ask sir about the naming convention/getters and setters for constant variables.
class Character(ABC):
    """
    Abstract class representating the base character
    """
    # Attributes
    __MAX_LEVEL = 50
    __LVLUP_ATK_INCR = 2
    __LVLUP_DEF_INCR = 2
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
    __world_speed = None
    # board position

    # Constructor
    def __init__(self, surf, rect, name, attack, defence, movement_points, level, experience_points, hit_points, max_health, weapon, is_alive, skills, world_speed):
        self.setSurf(surf)
        self.setRect(rect)
        self.setName(name)
        self.setAttack(attack)
        self.setDefence(defence)
        self.setMovementPoints(movement_points)
        self.setLevel(level)
        self.setExperiencePoints(experience_points)
        self.setHitPoints(hit_points)
        self.setMaxHealth(max_health)
        self.setWeapon(weapon)
        self.setIsAlive(is_alive)
        self.setSkills(skills)
        self.setWorldSpeed(world_speed)

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
    def getWorldSpeed(self):
        return self.__world_speed

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
    def setWorldSpeed(self, world_speed):
        self.__world_speed = world_speed

    # Methods
    def gainExperience(self, experience):
        """
        Increases character's experience, and increases levels accordingly. 
        Runs stat increase based on levels gained.
        """
        self.setExperiencePoints(self.getExperiencePoints() + experience)  # Increase character's experience points
        # Calculate experience required for next level
        required_experience = self.calcRequiredExperience()
        # Check if character has enough experience to level up and is below the level cap
        while self.getExperiencePoints() >= required_experience and self.getLevel() < self.getMaxLevel():
            self.setLevel(self.getLevel() + 1) # Level up the character
            self.setExperiencePoints(self.getExperiencePoints() - required_experience) # Decrease character's experience points
            # Calculate experience required for next level
            required_experience = self.calcRequiredExperience()
        print(f"Level up! {self.getName()} is now level {self.getLevel()}.")
        # TODO: Add stat increase function.

    def increaseStats(self):
        pass

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
