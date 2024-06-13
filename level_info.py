import pygame
from enemy import Enemy
from npc import Npc

class LevelInfo():
    """
    Class representing the level information: 
        - Stores level name and meta-info
        - Initialises all tiles and entities in world.
        - Stores tiles and their coordinates in a dictionary (position_tile_dict)
        - Stores entities (enemies/npcs) in groups (npc_group, enemy_group, portal_group)

    Attributes:
        level_name (str): Name of the current level
        all_clear (bool): True if all enemies are cleared, False otherwise.

        position_tile_dict (dict): Dictionary with coordinate tuple (xcoord, ycoord) keys with values being the tile type at the coordinate:
            {(xcoord, ycoord): tile_type}
        npc_group (pygame.sprite.Group): Group containing all npc sprites 
        enemy_group (pygame.sprite.Group): Group containing all enemy sprites
        portal_group (pygame.sprite.Group): Group containing all portal sprites
        all_sprites (pygame.sprite.Group): Pygame group containing all sprites [tiles, character, enemies, npcs]

    Constructor: ()
    
    Methods:
        initialiseLevel(self): Initialises level tiles and entities 
        parseLevelCode(self): Parses the code of the level with name level_name, and sets info in position_tile_dict 

    """


    # Methods
    def initialiseLevel(self):
        """
        Initialises the level's tiles and entities
        """


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
    


    def addEntityToGroup(self, tile_info):
        """
        Input tile_info: singular tuple representing a tile: (tile_code, xcoord, ycoord)
        Interprets tile_info, then adds tile entity to tile_list.
        Adds enemy/npc entities on tile (if exists) to their respective groups.
        """

        tile_code = tile_info[0].split('_') # [tile_type, entity_type, entity_id] code in world_gen_file
        tile_type, entity_type, entity_id = tile_code[0], tile_code[1], tile_code[2]
        xcoord, ycoord = int(tile_info[1]), int(tile_info[2]) # coordinates of tile

        # Adding tile to tile_list
        if tile_type == 'G':
            self.getTileList().append(((0, 255, 0), xcoord, ycoord)) # (surf, type, xcoord, ycoord)
        elif tile_type == 'W':
            self.getTileList().append(((0, 0, 0), xcoord, ycoord))

        # Adding entity (if exists) to respective group
        if entity_type != '0' and entity_id != '00':
            entity_info = self.parseEntityInfo(entity_type, entity_id) # list containing necessary parameters for the entity
            if entity_type == 'E': # entity is an enemy with constructor:
                # (surf, name, attack, defence, max_health, hit_points, weapon, is_alive, xcoord, ycoord, movement_pattern, xp_yield, gold_yield)
                # creates enemy object using the attributes from entity_info: found in enemy_id_file
                new_enemy = Enemy(pygame.image.load(GAME_ASSETS[entity_info[0]]), entity_info[1], int(entity_info[2]), int(entity_info[3]), int(entity_info[4]), int(entity_info[4]), entity_info[5], True, xcoord, ycoord, entity_info[6], int(entity_info[7]), int(entity_info[8])) 
                self.getEnemyGroup().add(new_enemy) # adds new enemy to enemy_group

           
                new_npc = Npc(pygame.image.load(GAME_ASSETS[entity_info[0]]), entity_info[1], entity_info[2])
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