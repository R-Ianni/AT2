import pygame
import random

class Npc:
    """
    TODO get this sorted
    """
    # Attributes
    __surf = None
    __rect = None
    __name = None
    __dialogue = None

    # Constructor
    def __init__(self, surf, name, dialogue):
        self.setSurf(surf)
        self.setRect(rect)
        self.setName(name)
        self.setDialogue(dialogue)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getDialogue(self):
        return self.__dialogue

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setDialogue(self, dialogue):
        self.__dialogue = dialogue