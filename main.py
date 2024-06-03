import pygame
from title_screen import TitleScreen
from game_world import GameWorld
from button import Button
from assets import load_assets, GAME_ASSETS
from pygame.locals import *
from character import Character

load_assets()

# Constants
SCREEN = pygame.display.set_mode((1200, 800))

# TODO Ask sir whether it is necessary to have attributes representing the different classes that are to be used
# Else, instead since stuff is called a single time each, do we really need the objects to be put under attributes for good coding practice.
# IMPORTANT

class Game:
    """
    A class representing the game.

    Attributes:
        screen (pygame.display): Display on which all objects are sent.
        state (str): Represents the state the game is in: ['title_screen', 'game_world', 'game_menu']
        is_running (bool): Whether game loop is running or not.
    
    Constructor: (screen, state, is_running)
        
    Methods:
        handleTitleScreen(self): If state == 'title_screen', runs TitleScreen and changes state accordingly.
        handleGameWorld(self): If state == 'game_world', runs GameWorld and changes state accordingly.
        onCleanup(self): When game loop is exited, quits pygame. TODO save system.
        run(self): Runs the game main loop
    """

    # Attributes
    __screen = None # game display
    __state = None # State of game: ['title_screen', 'game_world', 'game_menu']
    __is_running = None
    # TODO add clock attribute for framerate

    # Constructor
    def __init__(self, screen, state, is_running):
        pygame.init() # Initialise pygame
        self.setScreen(screen)
        self.setState(state)
        self.setIsRunning(is_running)

    # Getters
    def getScreen(self):
        return self.__screen
    def getState(self):
        return self.__state
    def getIsRunning(self):
        return self.__is_running

    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setState(self, state):
        self.__state = state
    def setIsRunning(self, is_running):
        self.__is_running = is_running

    # Methods

    def handleTitleScreen(self):
        """
        Runs if state == 'title_screen'. Runs TitleScreen class.
        Returns 'quit' if quit button hit; Returns 'start' if start button hit.
        """
        title_screen = TitleScreen(SCREEN, pygame.sprite.Group(), True) # StartMenu object
        title_screen.run()
        result = title_screen.getOutput()
        if result == 'start':
            self.setState('game_world')
        elif result == 'quit':
            self.setIsRunning(False)
    

    def handleGameWorld(self):
        """
        Runs if state == 'game_world'. Runs GameWorld class
        Returns 'quit' if game is quit. Returns
        """
        game_world = GameWorld(SCREEN, 'worldgenerator.txt', 'explore', True, Character(pygame.image.load(GAME_ASSETS['blue_orb']), 'Bob', 25, 25, 1, 0, 100, 100, 'sword', True, 'www', 'n', 100))
        #TODO fix Character object init.
        result = game_world.run()
        if result == 'title_screen':
            self.setState('game_menu')
        elif result == 'quit':
            self.setIsRunning(False)
    

    def onCleanup(self):
        """
        Runs when game loop ends - is_running == False. Quits pygame.
        TODO make this save game
        """
        pygame.quit()

    def run(self):
        """
        Runs the game loop
        """
        while self.getIsRunning() == True:
            # Event handler for QUIT
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    self.setIsRunning(False)

            if self.getState() == 'title_screen':  # If the state is 'title_screen'
                self.handleTitleScreen()

            elif self.getState() == 'game_world':  # If the state is 'game_world'
                self.handleGameWorld()

        self.onCleanup() # Runs cleanup, TODO save game.

if __name__ == "__main__":
    game = Game(SCREEN, 'title_screen', True)
    game.run() # Run the game
