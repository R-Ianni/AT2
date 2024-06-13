import pygame 
from assets import GAME_ASSETS
from attack import Attack

class Weapon(pygame.sprite.Sprite): 
    """
    A class representing a weapon.

    Attributes:
        surf (pygame.Surface): The weapon surface.
        image (pygame.image): The weapon's image
        rect (pygame.Rect): The weapon surface's rectangle
        name (str): The name of the weapon
        attack_list (list): The list of attacks the weapon has
        entity_xcoord (int): The xcoord of the entity holding weapon
        entity_ycoord (int): The ycoord of the entity holding weapon

    Constructor: (weapon_id)

    Methods:
    TODO
    """

    # Attributes
    __surf = None
    __image = None
    __rect = None
    __name = None
    __attack_list = None
    __entity_xcoord = None
    __entity_ycoord = None

    # Constructor
    def __init__(self, weapon_id, entity_xcoord, entity_ycoord):

        # Interpreting file with weapon_id to get weapon_info
        with open('gameinfostorage/weapon_id.txt', 'r') as weapon_file:
                str_to_find = '!!' + weapon_id # !!{ID} marker
                file_lines = weapon_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains weapon id
                        weapon_info = [i for i in line.split('~')[1].split('/')] # Weapon information split into a list: [image, name, *attacks]
                        break
        
        try: # error handling if weapon_info does not exist
            bool(weapon_info)
        except:
            raise Exception(f"No weapon with ID {weapon_id} found, or weapon file info corrupted")

        image, name = weapon_info[0], weapon_info[1] # gets the image and name of weapon
        
        # Initialising weapon object.
        self.setSurf(pygame.Surface(64, 64))
        self.setImage(pygame.image.load(GAME_ASSETS[image]))
        self.setRect(self.getSurf().get_rect())
        self.setName(name)
        self.setAttackList(list())
        self.setEntityXcoord(entity_xcoord)
        self.setEntityYcoord(entity_ycoord)

        # Adds all attacks to the attack list.
        for attack_id in weapon_info[2:]:
            attack = Attack(attack_id)
            self.getAttackList().append(attack)

    # Getters
    def getSurf(self):
        return self.__surf
    def getImage(self):
        return self.__image
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getAttackList(self):
        return self.__attack_list
    def getEntityXcoord(self):
        return self.__entity_xcoord
    def getEntityYcoord(self):
        return self.__entity_ycoord

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setImage(self, image):
        self.__image = image
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setAttackList(self, attacks):
        self.__attack_list = attacks
    def setEntityXcoord(self, entity_xcoord):
        self.__entity_xcoord = entity_xcoord
    def setEntityYcoord(self, entity_ycoord):
        self.__entity_ycoord = entity_ycoord