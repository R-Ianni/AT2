import pygame
from startmenu import StartMenu
from gameworld import GameWorld
from button import Button
from assets import load_assets, GAME_ASSETS
from pygame.locals import *

load_assets()

# Constants
SCREEN = pygame.display.set_mode((1200, 800))



class Game:
    """
    A class representing the game.

    Attributes:
        SCREEN_WIDTH (int): Constant representating width of screen
        SCREEN_HEIGHT (int): Constant representating height of screen
        screen (pygame.display): Display on which all objects are sent.
        start_menu (StartMenu): Starting menu, to be called when game initialised
        game_world (GameWorld): Class that represents the world character is in
        game_menu (GameMenu): Class that represents the menu/pause screen ingame.
        state (str): Represents the state the game is in: ['start_menu', 'game_world', 'game_menu']
        is_running (bool): Whether game loop is running or not.
    
    Constructor: (screen, start_menu, game_world, game_menu, state, is_running)
        
    Methods:
        handleStartMenu(self): If state == 'start_menu', runs StartMenu and changes state accordingly.
        handleGameWorld(self): If state == 'game_world', runs GameWorld and changes state accordingly.
        handleGameMenu(self): If state == 'game_menu', runs GameMenu and changes state accordingly.
        onCleanup(self): When game loop is exited, quits pygame. TODO save system.
        run(self): Runs the game main loop
    """

    # Attributes
    __screen = None # game display
    __start_menu = None # StartMenu class
    __game_world = None # GameWorld class
    __game_menu = None # GameMenu class
    __state = None # State of game: ['start_menu', 'game_world', 'game_menu']
    __is_running = None
    # TODO add clock attribute for framerate

    # Constructor
    def __init__(self, screen, start_menu, game_world, game_menu, state, is_running):
        pygame.init() # Initialise pygame
        self.setScreen(screen)
        self.setStartMenu(start_menu)
        self.setGameWorld(game_world)
        self.setGameMenu(game_menu)
        self.setState(state)
        self.setIsRunning(is_running)

    # Getters
    def getScreen(self):
        return self.__screen
    def getStartMenu(self):
        return self.__start_menu
    def getGameWorld(self):
        return self.__game_world
    def getGameMenu(self):
        return self.__game_menu
    def getState(self):
        return self.__state
    def getIsRunning(self):
        return self.__is_running

    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setStartMenu(self, start_menu):
        self.__start_menu = start_menu
    def setGameWorld(self, game_world):
        self.__game_world = game_world
    def setGameMenu(self, game_menu):
        self.__game_menu = game_menu
    def setState(self, state):
        self.__state = state
    def setIsRunning(self, is_running):
        self.__is_running = is_running

    # Methods

    def handleStartMenu(self):
        """
        Runs if state == 'start_menu'. Runs StartMenu class.
        Returns 'quit' if quit button hit; Returns 'start' if start button hit.
        """
        self.getStartMenu().run()
        result = self.getStartMenu().getOutput()
        if result == 'start':
            self.setState('game_world')
        elif result == 'quit':
            self.setIsRunning(False)
    
    def handleGameWorld(self):
        """
        Runs if state == 'game_world'. Runs GameWorld class
        Returns 'quit' if game is quit. Returns
        """
        result = self.getGameWorld().run()
        if result == 'game_menu':
            self.setState('game_menu')
        elif result == 'quit':
            self.setIsRunning(False)
    
    def handleGameMenu(self):
        """
        Runs if state == 'game_menu'. Runs GameMenu class.
        TODO
        """
        pass
    
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

            if self.getState() == 'start_menu':  # If the state is 'start_menu'
                self.handleStartMenu()

            elif self.getState() == 'game_world':  # If the state is 'game_world'
                self.handleGameWorld()
            
            elif self.getState() == 'game_menu':  # If the state is 'game_menu'
                self.handleGameMenu()

        self.onCleanup() # Runs cleanup, TODO save game.

if __name__ == "__main__":
    game = Game(
        SCREEN, 
        StartMenu(SCREEN,
                  Button(pygame.image.load(GAME_ASSETS['start_button']).convert(), 'start', (600, 300)),
                  Button(pygame.image.load(GAME_ASSETS['exit_button']).convert(), 'quit', (600, 600)),
                  pygame.sprite.Group(),
                  True), # StartMenu object
        'game_world', # GameWorld object
        'game_menu', # GameMenu object
        'start_menu', # state
        True) # is_running
    
    game.run() # Run the game
