import pygame

class Button(pygame.sprite.Sprite):
    """
    Class for a generalised button
    TO USE: if event.type == pygame.MOUSEBUTTONDOWN, and event.button == 1, then return output
    
    Attributes:
        surf (pygame.image): Surface for the button.
        rect (pygame.Rect): Rectangle underlying the button.
        output (str): What the button should return when clicked
        coords (tuple: int, int): Coordinates of the centre of button

    Constructor: (button_image, output, coords)
    """

    # Attributes
    __surf = None
    __rect = None
    __output = None
    __coords = None

    # Constructor
    def __init__(self, button_image, output, coords):
        super().__init__()
        self.setSurf(button_image) # sets surface to be the inputted image
        self.setRect(self.getSurf().get_rect()) # rectangle of surface
        self.setOutput(output) # what button returns when clicked
        self.setCoords(coords) # coordinates for button
        self.getRect().center = self.getCoords() # sets centre of button to be inputted coords

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getOutput(self):
        return self.__output
    def getCoords(self):
        return self.__coords

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setOutput(self, output):
        self.__output = output
    def setCoords(self, coords):
        self.__coords = coords