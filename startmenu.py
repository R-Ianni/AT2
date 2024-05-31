import pygame
from pygame.locals import *
from assets import GAME_ASSETS
from button import Button

#
## COMPLETE
#

class StartMenu:
    """
    Class that represents the start menu.

    Attributes:
    screen: pygame.display
    start_button: Button
    quit_button: Button
    button_group: pygame.sprite.Group
    is_running: bool
    output: str

    Constructor: (screen)

    Methods:
    run(): runs start menu.
    Returns 'quit' if game is to quit, returns 'start' if game is to start.

    """
    # Attributes
    __screen = None 
    __start_button = None
    __quit_button = None 
    __button_group = None 
    __is_running = None
    __output = None

    # Constructor
    def __init__(self, screen):
        self.setScreen(screen)
        self.setStartButton(Button(pygame.image.load(GAME_ASSETS['start_button']).convert(), 'start', 600, 300))
        self.setQuitButton(Button(pygame.image.load(GAME_ASSETS['exit_button']).convert(), 'quit', 600, 600)) # TODO change the exit button to quit button
        self.setButtonGroup(pygame.sprite.Group())
        self.getButtonGroup().add(self.getStartButton()) # adds start button to button group
        self.getButtonGroup().add(self.getQuitButton()) # adds quit button to button group
        self.setIsRunning(True)

    # Getters
    def getScreen(self):
        return self.__screen
    def getStartButton(self):
        return self.__start_button
    def getQuitButton(self):
        return self.__quit_button
    def getButtonGroup(self):
        return self.__button_group
    def getIsRunning(self):
        return self.__is_running
    def getOutput(self):
        return self.__output

    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setStartButton(self, start_button):
        self.__start_button = start_button
    def setQuitButton(self, quit_button):
        self.__quit_button = quit_button
    def setButtonGroup(self, button_group):
        self.__button_group = button_group
    def setIsRunning(self, is_running):
        self.__is_running = is_running
    def setOutput(self, output):
        self.__output = output

    # Methods
    def run(self):
        """
        Runs game loop for menu class.
        """
        while self.getIsRunning() == True:
            # Pygame event handler
            for event in pygame.event.get(): 
                if event.type == QUIT: # handles quit
                    self.setOutput('quit')
                    self.setIsRunning(False)

                elif event.type == pygame.MOUSEBUTTONDOWN: # Checks if mouse button pressed
                    if event.button == 1: # Checks if it's left button
                        mouse_pos = pygame.mouse.get_pos()
                        buttons_pressed = [button for button in self.getButtonGroup() if button.getRect().collidepoint(mouse_pos)]
                        if len(buttons_pressed) == 1: # a button has been pressed
                            self.setOutput(buttons_pressed[0].getOutput()) # Sets output to the output of the button clicked.
                            self.setIsRunning(False) # Stops menu since button has been pressed
                        # TODO handling for if there are more than one buttons pressed:

            self.getScreen().fill((255, 255, 255))
            for button in self.getButtonGroup():
                self.getScreen().blit(button.getSurf(), button.getRect())

            pygame.display.flip() # updates pygame display
            
        return self.getOutput() # Returns 'quit' if pygame is to quit, and 'start' if start button pressed.