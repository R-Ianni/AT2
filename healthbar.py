import pygame

class HealthBar:
    def __init__(self, x, y, max_health, width, height):
        self.x = x
        self.y = y
        self.max_health = max_health
        self.width = width
        self.height = height
        self.current_health = max_health

    def UpdateHealth(self, damage):
        self.current_health = self.current_health - damage
        
    def DrawBar(self, surface):
        width = (self.current_health / self.max_health) * self.width
        rectangle_outline = pygame.Rect(self.x, self.y, self.width, self.height) 
        rectangle_fill = pygame.Rect(self.x, self.y, width, self.height)
        pygame.draw.rect(surface, (0, 255, 0), rectangle_fill)
        pygame.draw.rect(surface, (150, 100, 20), rectangle_outline, 2)







    