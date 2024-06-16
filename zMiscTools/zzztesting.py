import pygame
from pygame.locals import *
import time
## DONT TOUCH MODULES

run = True
pygame.init()


screen = pygame.display.set_mode((500,500))
font = pygame.font.Font(None, 32)
x=pygame.Surface((100, 100))

text = font.render('eeee', True, (0,0,0))
x = text.get_rect()
x.topleft = (10,100)

while run == True:
    # Event handler for QUIT
    screen.fill((255, 255, 255))
    for event in pygame.event.get(): 
        if event.type == QUIT:
            run = False

    screen.blit(text, x)
    pygame.display.flip()
    
                    
pygame.quit()
