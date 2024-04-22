import pygame


# 1 means physics object
# 0 means non physics object i.e. air

class Map:
    def __init__(self, tileMap):
        self.map = tileMap
        self.platform = pygame.image.load('assets/stone.png').convert()
        self.platform =  pygame.transform.scale(self.platform, (16,16))
        self.tile_size = 16
        

    def getCollision(self, pos, size):
        collision = {"up": 0, "left": 0, "right": 0, "down": 0}
        # Check collided with the edges of the map

        if (pos[1] + size[1]) // 16 > len(map) or map[(pos[1] + size[1]) // 16][pos[0] // 16] == 1:
            collision["down"] = 1
        if (pos[1] // 16 < 0) or map[pos[1] // 16] == 1:
            collision["up"] = 1
        if ((pos[0] + size[0]) // 16 > len(map[0]) or map[]):
            collision["right"] = 1
        if (pos[0] // 16 < 0):
            collision["left"] = 1
        return collision
    
    def render(self, surf):
        # print(self.map)
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if (int(self.map[i][j]) == 1):
                    surf.blit(self.platform, (self.tile_size*j, self.tile_size*i))
