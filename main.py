import pygame
from startmenu import StartMenu
from character_select import CharacterSelect
from map import GameMap
from assets import load_assets, GAME_ASSETS
from pygame.locals import *

#
# COMPLETE FOR NOW
#

class Game:
    # Attributes
    __SCREEN_WIDTH = 1200
    __SCREEN_HEIGHT = 900
    __screen = None # game display
    __start_menu = None # StartMenu class
    __game_map = None # GameMap class
    __battle = None # Battle class
    __state = None # State of game: ['startmenu', 'gamemap', 'battle'] # TODO pause state
    __is_running = None

    # Constructor
    def __init__(self):
        pygame.init() # Initialise pygame
        load_assets() # load game image assets
        self.setScreen(pygame.display.set_mode((self.__SCREEN_WIDTH, self.__SCREEN_HEIGHT)))
        self.setStartMenu(StartMenu(self.getScreen()))
        #self.setGameMap(GameMap(self.getScreen()))
        #self.setBattle(Battle(self.getScreen()))
        self.setState('startmenu')
        self.setIsRunning(True)

    # Getters
    def getScreen(self):
        return self.__screen
    def getStartMenu(self):
        return self.__start_menu
    def getGameMap(self):
        return self.__game_map
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
    def setGameMap(self, game_map):
        self.__game_map = game_map
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
            self.setState('gamemap')
        elif result == 'quit':
            self.setIsRunning(False)
    
    def handleGameMap(self):
        """
        Runs if state == 'gamemap'. Runs GameMap class
        Returns 'quit' if game is quit; Returns 'battle' if battle is started
        """
        result = self.getGameMap().run()
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

            elif self.getState() == 'gamemap':  # If the state is 'game_map'
                self.handleGameMap()
            
            elif self.getState() == 'battle':  # If the state is 'battle'
                self.handleBattle()

        self.onCleanup() # Runs cleanup, TODO save game.

if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.run()  # Run the game
