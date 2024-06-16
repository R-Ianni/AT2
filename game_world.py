import pygame
from assets import GAME_ASSETS
from pygame.locals import *
from enemy import Enemy
from npc import Npc
from character import Character
from level_info import LevelInfo

# TODO create separate classes for all the different states.
# TODO make it so you actually can't go backwards once you have started a dungeon to make loading easier.
class GameWorld:
    """
    Class representing the game world
    Attributes:
        screen (pygame.display): Pygame display.
        state (str): Represents state GameWorld is in: [world, narrator, interaction, game_menu] TODO skill_menu, etc.
        is_running (bool): Whether the GameWorld loop is to keep running or finished.
        output (str): Output to be returned to main once loop finished. Represents next state game will enter:
            ['startmenu' -> exit and run StartMenu, 'quit' -> end game loop]
        
        character (Character): Character object controlled by player
        level_info (LevelInfo): Initialises and tracks tile and entity information in a level.
        foo (Foo): Gui interface with action selections


        # TODO fix attributes, from top-down view. Why am I working bottom up
        

    Constructor: (screen, world_gen_file, state, is_running, output, character, all_sprites, tile_group, npc_group, enemy_group)


    Methods: TODO
        handleWorld(self): Handles state where character is in world
        handleMenu(self, menu_type): 
        handleDisplay(self)
        run(): Game loop for game world
        TODO all methods

    """

    # Attributes
    __screen = None
    __state = None
    __is_running = None
    __character = None
    __current_level = None
    __output = None
    __all_sprites = None
    __tile_group = None
    __npc_group = None
    __enemy_group = None
    
    # Constructor
    def __init__(self, 
                 screen: pygame.Surface, 
                 state: str, 
                 is_running: bool, 
                 character: Character, 
                 current_level: int, 
                 output: str = 'quit', 
                 all_sprites = pygame.sprite.Group, 
                 tile_group = pygame.sprite.Group, 
                 npc_group = pygame.sprite.Group, 
                 enemy_group = pygame.sprite.Group):
        self.setScreen(screen)
        self.setState(state)
        self.setIsRunning(is_running)
        self.setCharacter(character)
        self.setCurrentLevel(current_level)
        self.setOutput(output)
        self.setAllSprites(all_sprites)
        self.setTileGroup(tile_group)
        self.setNpcGroup(npc_group)
        self.setEnemyGroup(enemy_group)


    # Getters
    def getScreen(self):
        return self.__screen
    def getState(self):
        return self.__state
    def getIsRunning(self):
        return self.__is_running
    def getCharacter(self):
        return self.__character
    def getCurrentLevel(self):
        return self.__current_level
    def getOutput(self):
        return self.__output
    def getAllSprites(self):
        return self.__all_sprites
    def getTileGroup(self):
        return self.__tile_group
    def getNpcGroup(self):
        return self.__npc_group
    def getEnemyGroup(self):
        return self.__enemy_group

    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setState(self, state):
        self.__state = state
    def setIsRunning(self, is_running):
        self.__is_running = is_running
    def setCharacter(self, character):
        self.__character = character
    def setCurrentLevel(self, current_level):
        self.__current_level = current_level
    def setOutput(self, output):
        self.__output = output
    def setAllSprites(self, all_sprites):
        self.__all_sprites = all_sprites
    def setTileGroup(self, tile_group):
        self.__tile_group = tile_group
    def setNpcGroup(self, npc_group):
        self.__npc_group = npc_group
    def setEnemyGroup(self, enemy_group):
        self.__enemy_group = enemy_group

    def handleWorld(self):
        pass
    
    def handleActionMenu(self):
        pass
    
    def handleNarrator(self, text):
        pass

    def handleInteraction(self, text, npc):
        pass

    def interpretButton(self):
        pass

    def handleDisplay(self):
        """
        Blits all objects onto the screen, and flips display
        """
        self.getScreen().fill((255, 255, 255)) # fills screen with white - overrides previous iteration's blits.
        for object in self.getAllSprites():
            self.getScreen().blit(object.getSurf(), object.getRect()) # blits all objects onto screen

        pygame.display.flip() # updates pygame display


    # Methods
    def run(self):
        """
        Runs the game world loop.
        Game world includes all stuff happening ingame after start button has been pressed.
        """
        while self.getIsRunning():
            while self.getIsRunning() == True:
            # Event handler for QUIT
                for event in pygame.event.get(): 
                    if event.type == QUIT:
                        self.setIsRunning(False)
                self.handleExplore()
            
        return self.getOutput()

        # TODO use pygame.event == KEYDOWN to do stuff with one movement at a time.