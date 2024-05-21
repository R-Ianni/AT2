from abc import ABC, abstractmethod

class Character(ABC):
    """
    Abstract class representating the base character
    """
    # Attributes
    __MAX_LEVEL: int = 50  # Maximum level a character can reach TODO: Ask sir whether this needs to be private
    __name: str = None # Name of character
    __character_class: str = None # Character's class
    __armor: int = None # Character's armor value
    __level: int = 1 # Character's current level
    __experience_points: int = 0 # Character's experience points
    __hit_points: int = None # Character's current hit points
    __max_health: int = None # Character's max health
    __skills: dict = {} # Character's skills
    __inventory: list = [] # Character's inventory
    __gold: int = 0 # Character's gold
    __is_alive:bool = True

    # Constructor
    def __init__(self, name, character_class, armor, max_health):
        self.setName(name) 
        self.setCharacterClass(character_class) 
        self.setArmor(armor) 
        self.setMaxHealth(max_health)
        self.setHitPoints(max_health)

    # Getters
    def getName(self):
        return self.__name
    def getCharacterClass(self):
        return self.__character_class
    def getLevel(self):
        return self.__level
    def getArmor(self):
        return self.__armor
    def getExperiencePoints(self):
        return self.__experience_points
    def getHitPoints(self):
        return self.__hit_points
    def getMaxHealth(self):
        return self.__max_health
    def getSkills(self):
        return self.__skills
    def getInventory(self):
        return self.__inventory
    def getGold(self):
        return self.__gold
    def getIsAlive(self):
        return self.__is_alive
    def getMaxLevel(self):
        return self.__MAX_LEVEL

    # Setters
    def setName(self, name):
        self.__name = name
    def setCharacterClass(self, character_class):
        self.__character_class = character_class
    def setLevel(self, level):
        self.__level = level
    def setArmor(self, armor):
        self.__armor = armor
    def setExperiencePoints(self, experience_points):
        self.__experience_points = experience_points
    def setHitPoints(self, hit_points):
        self.__hit_points = hit_points
        if self.getHitPoints() <= 0: # If health zero or negative, sets health to 0 and character to dead.
            self.setHitPoints(0)
            self.setIsAlive(False)
    def setMaxHealth(self, max_health):
        self.__max_health = max_health
    def setSkills(self, skills):
        self.__skills= skills
    def setInventory(self, inventory):
        self.__inventory = inventory
    def setGold(self, gold):
        self.__gold = gold
    def setIsAlive(self, is_alive):
        self.__is_alive = is_alive 

    # Methods
    def gainExperience(self, experience):
        """
        Increases character's experience, and increases levels accordingly. 
        Runs stat increase based on levels gained.
        """
        self.setExperiencePoints(self.getExperiencePoints() + experience)  # Increase character's experience points
        # Calculate experience required for next level
        required_experience = self.calculateRequiredExperience(self.getLevel())
        # Check if character has enough experience to level up and is below the level cap
        while self.getExperiencePoints() >= required_experience and self.getLevel() < self.getMaxLevel():
            self.setLevel(self.getLevel() + 1) # Level up the character
            self.setExperiencePoints(self.getExperiencePoints() - required_experience) # Decrease character's experience points
            # Calculate experience required for next level
            required_experience = self.calculateRequiredExperience(self.getLevel())
        print(f"Level up! {self.getName()} is now level {self.getLevel()}.")
        # TODO: Add stat increase function.

    def calculateRequiredExperience(self, level): # level = current level
        """
        Calculates total required experience to get to next level
        """
        return int(100 * (1.5 ** (level)))

    def takeDamage(self, amount): # amount = raw damage
        """
        Calculate the actual damage taken, taking into account the character's armor.
        Then subtract from character's hitpoint.
        """
        actual_damage = max(0, amount - self.armor)
        self.setHitPoints(self.getHitPoints() - actual_damage)
        if self.getHitPoints() <= 0:
            self.setIsAlive(False)
            print(f"{self.getName()} takes {actual_damage} damage and has been defeated!")
        else:
            print(f"{self.getName()} takes {actual_damage} damage. Remaining hit points: {self.getHitPoints()}/{self.getMaxHealth()}")
