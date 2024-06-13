import pygame
from assets import GAME_ASSETS

class Npc(pygame.sprite.Sprite):
    """
    Attributes:
        surf (pygame.Surface): Surface of npc
        image (pygame.image): Image for npc
        rect (pygame.Rect): Rectangle representing position of npc surface
        name (str): Name of npc
        dialogue (str): Dialogue npc says
        xcoord (int): xcoord of npc
        ycoord (int): ycoord of npc
    """

    # Attributes
    __surf = None
    __image = None
    __rect = None
    __name = None
    __dialogue = None
    __xcoord = None
    __ycoord = None

    # Constructor
    def __init__(self, npc_id, xcoord, ycoord):
        # Interpreting file with npc_id to get npc_info
        with open('gameinfostorage/npc_id.txt', 'r') as npc_file:
                str_to_find = '!!' + npc_id # !!{ID} marker
                file_lines = npc_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains npc id
                        npc_info = [i for i in line.split('~')[1].split('/')] # Npc information split into a list: [image, name, ]
                        break
        
        try: # error handling if npc_info does not exist
            bool(npc_info)
        except:
            raise Exception(f"No npc with ID {npc_id} found, or npc file info corrupted")

        image, name, dialogue = npc_info # unpacks all npc information
        
        # Initialising npc object.
        super().__init__()
        self.setSurf(pygame.Surface(64, 64))
        self.setImage(pygame.image.load(GAME_ASSETS[image]))
        self.setRect(self.getSurf().get_rect())
        self.setName(name)
        self.setDialogue(dialogue)
        self.setXcoord(xcoord)
        self.setYcoord(ycoord)


    # Getters
    def getSurf(self):
        return self.__surf
    def getImage(self):
        return self.__image
    def getRect(self):
        return self.__rect
    def getName(self):
        return self.__name
    def getDialogue(self):
        return self.__dialogue
    def getXcoord(self):
        return self.__xcoord
    def getYcoord(self):
        return self.__ycoord

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setImage(self, image):
        self.__image = image
    def setRect(self, rect):
        self.__rect = rect
    def setName(self, name):
        self.__name = name
    def setDialogue(self, dialogue):
        self.__dialogue = dialogue
    def setXcoord(self, xcoord):
        self.__xcoord = xcoord
    def setYcoord(self, ycoord):
        self.__ycoord = ycoord