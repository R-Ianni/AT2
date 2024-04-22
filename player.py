import pygame

class Player:
    def __init__(self, type, pos, size):
        self.pos = pos
        self.size = size
        self.type = type
        self.sprite = pygame.image.load('assets/player.png').convert()
        self.sprite = pygame.transform.scale(self.sprite, size)
        self.velocity = [0, 0]

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, movement, map):
        new_x = self.pos[0] + movement[0]
        new_y = self.pos[1] + movement[1]

        # collisions = map.getCollision([new_x, new_y], self.size)
        collisions = {"up": 0, "left": 0, "right": 0, "down": 0}
        # Adjust the x coordinate
        if collisions["left"] == 0 and movement[0] < 0:
            self.pos[0] = new_x
        elif collisions["right"] == 0 and movement[0] > 0:
            self.pos[0] = new_x

        # Adjust the y coordinate
        if collisions["up"] == 0 and movement[1] < 0:
            self.pos[0] = new_y
        elif collisions["down"] == 0 and movement[1] > 0:
            self.pos[1] = new_y
        
        # Apply gravity
        if collisions["down"] == 0:
            self.pos[1] -= 1
        

    def render(self, surf):
        surf.blit(self.sprite, self.pos)
    