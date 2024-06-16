import pygame
from pygame.locals import *
from assets import GAME_ASSETS
from file_id_interpreter import FileIdInterpreter

class Portal(pygame.sprite.Sprite):
    """
    Class representing a portal object

    Attributes:
        surf (pygame.Surface): Surface representing the portal
        image (pygame.Image): Portal image
        rect (pygame.Rect): Rect representing position of portal on screen
        xcoord (int): Board xcoord of portal
        ycoord (int): Board ycoord of portal
        destination (str): Represents the level portal leads to

    Constructor: (portal_id, xcoord, ycoord)
    """

    # Attributes
    __surf = None
    __image = None
    __rect = None
    __xcoord = None
    __ycoord = None
    __destination = None

    # Constructor
    def __init__(self, portal_id: str, xcoord: int, ycoord: int):
        # Getting and unpacking file info
        file_interpreter = FileIdInterpreter('gameinfostorage/portal_id.txt', portal_id)
        destination, = file_interpreter.interpretFileInfo() 
        
        # Initialising portal object.
        super().__init__()
        self.setImage("portal image ") # TODO get portal image asset
        self.setRect(self.getSurf().get_rect())
        self.setXcoord(xcoord)
        self.setYcoord(ycoord)
        self.setDestination(destination)
        self.setSurf(pygame.Surface((64, 64), SRCALPHA))

    # Getters
    def getSurf(self):
        return self.__surf
    def getImage(self):
        return self.__image
    def getRect(self):
        return self.__rect
    def getXcoord(self):
        return self.__xcoord
    def getYcoord(self):
        return self.__ycoord
    def getDestination(self):
        return self.__destination

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setImage(self, image):
        self.__image = image
    def setRect(self, rect):
        self.__rect = rect
    def setXcoord(self, xcoord):
        self.__xcoord = xcoord
    def setYcoord(self, ycoord):
        self.__ycoord = ycoord
    def setDestination(self, destination):
        self.__destination = destination
