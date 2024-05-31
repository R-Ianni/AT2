import pygame
from startmenu import StartMenu
from gameworld import GameWorld
from button import Button
from assets import load_assets, GAME_ASSETS
from pygame.locals import *

load_assets()

# Constants
SCREEN = pygame.display.set_mode(())



class Game:
    """
    A class representing the game.

    Attributes:
        SCREEN_WIDTH (int): Constant representating width of screen
        SCREEN_HEIGHT (int): Constant representating height of screen
        screen (pygame.display): Display on which all objects are sent.
        start_menu (StartMenu): Starting menu, to be called when game initialised
        game_world (GameWorld): Class that represents the world character is in
        battle (Battle): Class that represents when the character is in a battle
        state (str): Represents the state the game is in: ['startmenu', 'gameworld', 'battle'] TODO 'pause'
        is_running (bool): Whether game loop is running or not.
        
    Methods:
        handleStartMenu(self): If state == 'startmenu', runs StartMenu and changes state accordingly.
        handleGameWorld(self): If state == 'gameworld', runs GameWorld and changes state accordingly.
        handleBattle(self): If state == 'battle', runs Battle and changes state accordingly.
        onCleanup(self): When game loop is exited, quits pygame. TODO save system.
        run(self): Runs the game main loop
    """

    # Attributes
    __screen = None # game display
    __start_menu = None # StartMenu class
    __game_world = None # GameWorld class
    __battle = None # Battle class
    __state = None # State of game: ['startmenu', 'gameworld', 'battle'] # TODO pause state
    __is_running = None
    # TODO add clock attribute for framerate

    # Constructor
    def __init__(self, screen, start_menu, game_world, battle, state, is_running):
        pygame.init() # Initialise pygame
        self.setScreen(screen)
        self.setStartMenu(start_menu)
        self.setGameWorld(game_world)
        self.setBattle(battle)
        self.setState(state)
        self.setIsRunning(is_running)

    # Getters
    def getScreen(self):
        return self.__screen
    def getStartMenu(self):
        return self.__start_menu
    def getGameWorld(self):
        return self.__game_world
    def getBattle(self):
        return self.__battle
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
    def setBattle(self, battle):
        self.__battle = battle 
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
            self.setState('gameworld')
        elif result == 'quit':
            self.setIsRunning(False)
    
    def handleGameWorld(self):
        """
        Runs if state == 'gameworld'. Runs GameWorld class
        Returns 'quit' if game is quit; Returns 'battle' if battle is started
        """
        result = self.getGameWorld().run()
        if result == 'battle':
            self.setState('battle')
        elif result == 'quit':
            self.setIsRunning(False)
    
    def handleBattle(self):
        """
        Runs if state == 'battle'. Runs Battle class.
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

            if self.getState() == 'startmenu':  # If the state is 'startmenu'
                self.handleStartMenu()

            elif self.getState() == 'gameworld':  # If the state is 'gameworld'
                self.handleGameWorld()
            
            elif self.getState() == 'battle':  # If the state is 'battle'
                self.handleBattle()

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
        'battle', # Battle object
        'startmenu', # state
        True) # is_running
    
    game.run() # Run the game
