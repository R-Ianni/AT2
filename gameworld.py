import pygame
from assets import GAME_ASSETS
from pygame.locals import *
# TODO make text file coordinate interpreter of worlds. I want a world system that is a board. Battle can just happen randomly during them.
class GameWorld:
    """
    Class representing the game world
    Attributes:
        screen (pygame.display): Pygame display.
        world_file (str): File that contains the initial tile positions for a backdrop (also needs to track npcs, enemy initial positions)
        state (str): Represents state GameWorld is in: [explore, battle, action_menu, narrator, interaction, game_menu] TODO skill_menu, etc.
        turn_tracker (str): During battle, tracks whether it is user_turn or enemy_turn.
        is_running (bool): Whether the GameWorld loop is to keep running or finished.
        output (str): Output to be returned to main once loop finished. Represents next state game will enter:
            ['startmenu' -> exit and run StartMenu, 'quit' -> end game loop]
        
        character (Character): Character object controlled by player
        all_sprites (pygame.sprite.Group): Pygame group containing all sprites [tiles, character, enemies, npcs]
        tile_group (pygame.sprite.Group): Group containing all tile sprites
        npc_group (pygame.sprite.Group): Group containing all npc sprites
        enemy_group (pygame.sprite.Group): Group containing all enemy sprites
        
        game_menu (GameMenu): Class that represents the menu/pause screen ingame.


    Constructor: (screen, character, all_sprites, tile_group, npc_group, enemy_group, world_file, internal_state, is_running, output)

    Methods:
        handleExplore(self): Handles state where character is moving and not in battle
        run(): Game loop for game world

    """


    # Attributes
    __screen = None
    __character = None
    __all_sprites = None
    __tile_group = None
    __npc_group = None
    __enemy_group = None
    __world_file = None
    __internal_state = None
    __turn_tracker = None
    __is_running = None
    __output = None

    # Constructor
    def __init__(self, screen, character, all_sprites, tile_group, npc_group, enemy_group, world_file, internal_state, turn_tracker, is_running, output):
        self.setScreen(screen)
        self.setCharacter(character)
        self.setAllSprites(all_sprites)
        self.setTileGroup(tile_group)
        self.setNpcGroup(npc_group)
        self.setEnemyGroup(enemy_group)
        self.setWorldFile(world_file)
        self.setInternalState(internal_state)
        self.setTurnTracker(turn_tracker)
        self.setIsRunning(is_running)
        self.setOutput(output)

    # Getters
    def getScreen(self):
        return self.__screen
    def getCharacter(self):
        return self.__character
    def getAllSprites(self):
        return self.__all_sprites
    def getTileGroup(self):
        return self.__tile_group
    def getNpcGroup(self):
        return self.__npc_group
    def getEnemyGroup(self):
        return self.__enemy_group
    def getWorldFile(self):
        return self.__world_file
    def getInternalState(self):
        return self.__internal_state
    def getTurnTracker(self):
        return self.__turn_tracker
    def getIsRunning(self):
        return self.__is_running
    def getOutput(self):
        return self.__output

    # Setters
    def setScreen(self, screen):
        self.__screen = screen
    def setCharacter(self, character):
        self.__character = character
    def setAllSprites(self, all_sprites):
        self.__all_sprites = all_sprites
    def setTileGroup(self, tile_group):
        self.__tile_group = tile_group
    def setNpcGroup(self, npc_group):
        self.__npc_group = npc_group
    def setEnemyGroup(self, enemy_group):
        self.__enemy_group = enemy_group
    def setWorldFile(self, world_file):
        self.__world_file = world_file
    def setInternalState(self, internal_state):
        self.__internal_state = internal_state
    def setTurnTracker(self, turn_tracker):
        self.__turn_tracker = turn_tracker
    def setIsRunning(self, is_running):
        self.__is_running = is_running
    def setOutput(self, output):
        self.__output = output
        
    def handleExplore(self):
        pass
    
    def handleBattle(self):
        pass

    def handleActionMenu(self):
        pass
    
    def handleNarrator(self, text):
        pass

    def handleInteraction(self, text, npc):
        pass

    def interpretButton(self):
        pass

    # Methods
    def run(self):
        """
        Runs the game world loop.
        Game world includes all stuff happening ingame after start button has been pressed.
        """



        # TODO use pygame.event == KEYDOWN to do stuff.