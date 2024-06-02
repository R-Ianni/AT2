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

        surf (pygame.image): Pygame surface image for the character
        rect (pygame.Rect): Rectangle representing character surface position
        name (str): Name of character
        attack (int): Attack stat
        defence (int): Defence stat
        level (int): Level stat
        experience points (int): Experience point stat
        hit_points (int): Current hit points stat
        max_health (int): Maximum hit points stat
        weapon (Weapon): Currently held weapon
        is_alive (bool): Whether character's hit points above 0 or not
        skills (list: Skills): List of skills the character has

    Constructor: (surf, name, attack, defence, level, experience_points, hit_points, max_health, weapon, is_alive, skills)

    Methods:
        gainExperience(self, experience): 
        updateStats(self)
        calcRequiredExperience(self)
        takeDamage(self, damage)
        updatePosition(self, pressed_keys)
    """
    
    # Attributes
    MAX_LEVEL = 50
    LVLUP_ATK_INCR = 2
    LVLUP_DEF_INCR = 2
    __surf = None
    __rect = None
    __name = None
    __attack = None
    __defence = None
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
    # Character(pygame.image.load(GAME_ASSETS['blue_orb'], 'Bob', 25, 25, 1, 0, 1000, 1000, 'sword', True, 'www')

    # Constructor
    def __init__(self, surf, name, attack, defence, level, experience_points, hit_points, max_health, weapon, is_alive, skills):
        self.setSurf(surf)
        self.setRect(self.getSurf().get_rect())
        self.setName(name)
        self.setAttack(attack)
        self.setDefence(defence)
        self.setLevel(level)
        self.setExperiencePoints(experience_points)
        self.setHitPoints(hit_points)
        self.setMaxHealth(max_health)
        self.setHitPoints(self.getMaxHealth())
        self.setWeapon(weapon) # TODO replace with starter weapon / character initialisation screen.
        self.setIsAlive(is_alive)
        self.setSkills(skills)

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
    def setLevel(self, level):
        self.__level = level
    def setExperiencePoints(self, experience_points):
        self.__experience_points = experience_points
    def setHitPoints(self, hit_points):
        max_health = self.getMaxHealth() 
        if hit_points > max_health: # ensures 0 <= hit_points <= max_health
            self.__hit_points = max_health
        elif hit_points < max_health:
            self.__hit_points = 0
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

    def takeDamage(self, amount): # amount = raw damage
        """
        Calculate the actual damage taken, taking into account the character's defence.
        Then subtract from character's hitpoint.
        """
        actual_damage = max(0, amount - self.defence) # TODO change formula
        self.setHitPoints(self.getHitPoints() - actual_damage)
        if self.getHitPoints() <= 0:
            self.setIsAlive(False)
            print(f"{self.getName()} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.getName()} takes {actual_damage} damage. Remaining hit points: {self.getHitPoints()}/{self.getMaxHealth()}")

    def updatePosition(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.getRect().moveip((-5, 0))
        if pressed_keys[K_RIGHT]:
            self.getRect().moveip((5, 0))
        if pressed_keys[K_UP]:
            self.getRect().moveip((0, -5))
        if pressed_keys[K_DOWN]:
            self.getRect().moveip((0, 5))