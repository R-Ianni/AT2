import pygame

class Button(pygame.sprite.Sprite):
    """
    Class for a generalised button
    TO USE: if event.type == pygame.MOUSEBUTTONDOWN, and event.button == 1, then return output
    
    Attributes:
        surf (pygame.Surface): Surface for the button.
        rect (pygame.Rect): Rectangle underlying the button.
        text (str): What the button says on it
        colour (tuple[int, int, int]): Colour of button
        output (str): What the button should return when activated (clicked/connected_key pressed)
        centre_coords (tuple[int, int]): Coordinates of the centre of button
        connected_key (str): Key that when pressed should activate the button.

    Constructor: (surf, text, colour, output, centre_coords, connected_key = None)
    
    Methods:
        initialiseButtonSurf(self): creates button surface, 
    """

    # Attributes
    __surf = None
    __rect = None
    __text = None
    __colour = None
    __output = None
    __centre_coords = None
    __connected_key = None

    # Constructor
    def __init__(self, 
                 surf: pygame.Surface, 
                 text: str,
                 colour: tuple[int, int, int], 
                 output: str, 
                 centre_coords: tuple[int, int], 
                 connected_key: str = None):
        super().__init__()
        self.setSurf(surf)
        self.setRect(self.getSurf().get_rect())
        self.setText(text)
        self.setColour(colour)
        self.setOutput(output)
        self.setCentreCoords(centre_coords)
        self.setConnectedKey(connected_key)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getText(self):
        return self.__text
    def getColour(self):
        return self.__colour
    def getOutput(self):
        return self.__output
    def getCentreCoords(self):
        return self.__centre_coords
    def getConnectedKey(self):
        return self.__connected_key

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setText(self, text):
        self.__text = text
    def setColour(self, colour):
        self.__colour = colour
    def setOutput(self, output):
        self.__output = output
    def setCentreCoords(self, centre_coords):
        self.__centre_coords = centre_coords
    def setConnectedKey(self, connected_key):
        self.__connected_key = connected_key

