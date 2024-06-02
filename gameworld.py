import pygame
from assets import GAME_ASSETS
from pygame.locals import *
# TODO make text file coordinate interpreter of worlds. I want a world system that is a board. Battle can just happen randomly during them.
class GameWorld:
    """
    Class representing the game world
    Attributes:
        screen (str): 
        character (Character):
        world_file (str): The file that contains the initial world/background information for a particular place (also needs to track npcs, enemies)
        state (str): Represents state Gameworld is in: [options, ingame, TODO interaction?]
        character (Character): Character object, controlled by player
        game_menu (GameMenu): GameMenu object, represents the game menu.
        is_running (bool): Whether the game loop is to keep running or finished.
        output (str): Output to be returned to main once loop finished. Represents next state game will enter:
            ['game_menu' -> run GameMenu, 'quit' -> end game loop]

    Constructor:

    Methods:
        run(): Game loop for game world

    """

    # Attributes
    __world_file = None
    __state = None
    __character = None
    __game_menu = None
    __is_running = None
    __output = None

    # Constructor
    def __init__(self, world_file, state, character, game_menu, is_running, output):
        self.setWorldFile(world_file)
        self.setState(state)
        self.setCharacter(character)
        self.setGameMenu(game_menu)
        self.setIsRunning(is_running)
        self.setOutput(output)

    # Getters
    def getWorldFile(self):
        return self.__world_file
    def getState(self):
        return self.__state
    def getCharacter(self):
        return self.__character
    def getGameMenu(self):
        return self.__game_menu
    def getIsRunning(self):
        return self.__is_running
    def getOutput(self):
        return self.__output

    # Setters
    def setWorldFile(self, world_file):
        self.__world_file = world_file
    def setState(self, state):
        self.__state = state
    def setCharacter(self, character):
        self.__character = character
    def setGameMenu(self, game_menu):
        self.__game_menu = game_menu
    def setIsRunning(self, is_running):
        self.__is_running = is_running
    def setOutput(self, output):
        self.__output = output


    # Methods
    def run(self):
        """
        Runs the game world loop.
        Game world includes all stuff happening ingame after start button has been pressed.
        """



        # TODO use pygame.event == KEYDOWN to do stuff.