import pygame
from enemy import Enemy
from npc import Npc

# TODO Make it return not tile, but rather a tuple representing tile colour, tile x coord and tile y coord
# TODO In GameWorld, we can blit all the tiles onto a background surface first, then just blit the background surface whenever it updates.
class WorldGenInterpreter:
    """
    Class that gives backdrop info by interpreting worldgenerator.txt, and returns a group of tiles, enemies and npcs.
    TO USE: use method translateLevelCode(), then get tile_list, enemy_group, npc_group.

    Attributes:
        world_gen_file (str): string that represents the file containing code for backdrops
        enemy_id_file (str): string that represents file containing dictionary of enemy information
        npc_id_file (str): string that represents file containing dictionary of npc information
        level_name (str): string that represents the level player is on
        tile_list (list): List that contains tuples representing tile information: (Colour:RGB, xcoord, ycoord)
        enemy_group (pygame.sprite.Group): Group that represents the enemy objects for the current level.
        npc_group (pygame.sprite.Group): Group that represents the npc objects for the current level.

    Constructor: (world_gen_file, enemy_id_file, npc_id_file, level_name)

    Methods:
        parseLevelCode(self): Finds 12x12 levels code in world_gen_file, and returns it as a list of tuples: (tile_code, xcoord, ycoord), zero-indexed
        parseEntityInfo(self, entity_type, entity_id): Returns the entity object given by entity_type (npc/enemy), entity_id
        addEntityToGroup(self, tile_code): Adds tile to tile_list, and any additional entities to their respective groups
        translateLevelCode(self): Main function which carries out the translation of level code, and adds objects to tile_list, enemy_group, npc_group
    """

    # Attributes
    __world_gen_file = None
    __enemy_id_file = None
    __npc_id_file = None
    __level_name = None
    __tile_list = None
    __enemy_group = None
    __npc_group = None

    # Constructor
    def __init__(self, world_gen_file, enemy_id_file, npc_id_file, level_name, tile_list=list(), enemy_group=pygame.sprite.Group, npc_group=pygame.sprite.Group):
        self.setWorldGenFile(world_gen_file)
        self.setEnemyIdFile(enemy_id_file)
        self.setNpcIdFile(npc_id_file)
        self.setLevelName(level_name)
        self.setTileList(tile_list)
        self.setEnemyGroup(enemy_group)
        self.setNpcGroup(npc_group)

    # Getters
    def getWorldGenFile(self):
        return self.__world_gen_file
    def getEnemyIdFile(self):
        return self.__enemy_id_file
    def getNpcIdFile(self):
        return self.__npc_id_file
    def getLevelName(self):
        return self.__level_name
    def getTileList(self):
        return self.__tile_list
    def getEnemyGroup(self):
        return self.__enemy_group
    def getNpcGroup(self):
        return self.__npc_group

    # Setters
    def setWorldGenFile(self, world_gen_file):
        self.__world_gen_file = world_gen_file
    def setEnemyIdFile(self, enemy_id_file):
        self.__enemy_id_file = enemy_id_file
    def setNpcIdFile(self, npc_id_file):
        self.__npc_id_file = npc_id_file
    def setLevelName(self, level_name):
        self.__level_name = level_name
    def setTileList(self, tile_list):
        self.__tile_list = tile_list
    def setEnemyGroup(self, enemy_group):
        self.__enemy_group = enemy_group
    def setNpcGroup(self, npc_group):
        self.__npc_group = npc_group

    # Methods
    def parseLevelCode(self):
        """
        Finds 12x12 level code in file and returns a list of tuples of form: (tile_code, xcoord, ycoord)
        """
        str_to_find = '!!' + self.getLevelName() # !!{level_name} - marker line for world gen code
        with open(self.getWorldGenFile(), 'r') as world_gen_file:
            file_lines = world_gen_file.readlines()
            for pos, line in enumerate(file_lines):
                if str_to_find in line:
                    starting_pos = pos + 1 # position of line at which level code starts

                    # level_code_lines is a list of 12 lines representing each row of tile code
                    level_code_lines = [file_lines[starting_pos + i] for i in range(12)]
                    # tile_info is a list containing 144 tuples representing tile information
                    tile_info = [(tile_code, xcoord, ycoord) for xcoord, code_line in enumerate(level_code_lines) for ycoord, tile_code in enumerate(code_line.split())]
                    return tile_info

    def parseEntityInfo(self, entity_type, entity_id):
        """
        Inputs entity_type (npc: N, or enemy: E), entity_id. 
        Uses enemy_id_file and npc_id_file to get corresponding entity, the info of which it returns as a list
        """
        if entity_type == "E":
            with open(self.getEnemyIdFile(), 'r') as enemy_file:
                str_to_find = '!!' + entity_id
                file_lines = enemy_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains enemy id
                        enemy_info = [i for i in line.split('~')[1].split('/')] # Enemy information split into a list:
            return enemy_info # [surf, name, attack, defence, max_health, weapon, movement_pattern, xp_yield, gold_yield]

        elif entity_type == "N":
            with open(self.getNpcIdFile, 'r') as npc_file:
                str_to_find = '!!' + entity_id
                file_lines = npc_file.readlines()
                for line in file_lines:
                    if str_to_find in line: # if line contains npc id
                        npc_info = [i for i in line.split('~')[1].split('/')] # Npc information split into a list:
            return npc_info # [surf, name, dialogue]
        

    def addEntityToGroup(self, tile_info):
        """
        Input tile_info: singular tuple representing a tile: (tile_code, xcoord, ycoord)
        Interprets tile_info, then adds tile entity to tile_list.
        Adds enemy/npc entities on tile (if exists) to their respective groups.
        """

        tile_code = tile_info[0].split('_') # [tile_type, entity_type, entity_id] code in world_gen_file
        tile_type, entity_type, entity_id = tile_code[0], tile_code[1], tile_code[2]
        xcoord, ycoord = tile_info[1], tile_info[2] # coordinates of tile

        # Adding tile to tile_list
        if tile_type == 'G':
            self.getTileList().append(((0, 255, 0), xcoord, ycoord)) # (surf, type, xcoord, ycoord)
        elif tile_type == 'W':
            self.getTileList().append(((0, 0, 0), xcoord, ycoord))

        # Adding entity (if exists) to respective group
        if entity_type != '0' and entity_id != '00':
            entity_info = self.parseEntityInfo(entity_type, entity_id) # list containing necessary parameters for the entity
            if entity_type == 'E': # entity is an enemy with constructor:
                # (surf, name, attack, defence, hit_points, max_health, weapon, xcoord, ycoord, movement_pattern, xp_yield, gold_yield)
                # creates enemy object using the attributes from entity_info: found in enemy_id_file
                new_enemy = Enemy(entity_info[0], entity_info[1], entity_info[2], entity_info[3], entity_info[4], entity_info[4], entity_info[5], xcoord, ycoord, entity_info[6], entity_info[7], entity_info[8]) 
                self.getEnemyGroup().add(new_enemy) # adds new enemy to enemy_group

            elif entity_type == 'N': # entity is an npc with constructor: (surf, name, dialogue)
                new_npc = Npc(entity_info[0], entity_info[1], entity_info[2])
                self.getNpcGroup.add(new_npc)
                    


    def translateLevelCode(self):
        """
        Main method: translates 12x12 world code from world_gen_file, and adds the objects encoded to their respective group attributes
        """
        # level_code is the code in world_gen_file that represents the given level
        level_code = self.parseLevelCode()
        # tile_info is a tuple: (tile_code, xcoord, ycoord)
        for tile_info in level_code: # runs through all tiles in level_code
            self.addEntityToGroup(tile_info) # adds each tile and entities on it to their respective sprite groups.
        
new = WorldGenInterpreter('gameinfostorage/world_gen.txt', 'gameinfostorage/enemy_id.txt', 'gameinfostorage/npc_id.txt', 'Music Centre 1')
new.translateLevelCode()
print(new.getEnemyGroup().sprites)