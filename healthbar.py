import pygame

class Healthbar:
    """
    Class representing a healthbar sprite

    Attributes:

        surf (pygame.Surface): Represents
        rect (pygame.Rect): Position of 

        entity_health (int): TODO
        entity_max_hp (int):
        entity_xcoord (int):
        entity_ycoord (int):

    Constructor: TODO

    Methods:
        updatePosition(self): To be called whenever entity moves. Updates healthbar position.
        updateHealth(self): To be called whenever entity health changes. Updates healthbar surface.
    """

    # Attributes
    __surf = None
    __rect = None
    __entity_health = None
    __entity_max_hp = None
    __entity_xcoord = None
    __entity_ycoord = None

    # Constructor
    def __init__(self, surf: pygame.Surface, entity_health: int, entity_max_hp: int, entity_xcoord: int, entity_ycoord: int):
        self.setSurf(surf)
        self.setRect(self.getSurf().get_rect())
        self.setEntityHealth(entity_health)
        self.setEntityMaxHp(entity_max_hp)
        self.setEntityXcoord(entity_xcoord)
        self.setEntityYcoord(entity_ycoord)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getEntityHealth(self):
        return self.__entity_health
    def getEntityMaxHp(self):
        return self.__entity_max_hp
    def getEntityXcoord(self):
        return self.__entity_xcoord
    def getEntityYcoord(self):
        return self.__entity_ycoord

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setEntityHealth(self, entity_health):
        self.__entity_health = entity_health
    def setEntityMaxHp(self, entity_max_hp):
        self.__entity_max_hp = entity_max_hp
    def setEntityXcoord(self, entity_xcoord):
        self.__entity_xcoord = entity_xcoord
    def setEntityYcoord(self, entity_ycoord):
        self.__entity_ycoord = entity_ycoord
