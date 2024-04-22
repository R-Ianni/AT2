import sys

import pygame

from utils import load_image, load_images
from player import Player
from map import Map

BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('AT2 game')
        self.screen = pygame.display.set_mode((640, 320)) # 20 * 40 tileset
        self.screen.fill(BLACK)
        self.map = Map(['1111111111111111111111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1100000000000000001111111111111111111111',
                        '1111111111111111111111111111111111111111',])
        self.sprite_sheet = pygame.image.load('assets/industrial.png').convert()

        self.clock = pygame.time.Clock()

        self.player = Player('player', (50, 50), (20, 30))
        
        self.movement = [False, False]
        
        
    def run(self):
        while True:
            self.screen.fill((33, 36,51))
            # sprite = pygame.Surface((100, 26))
            # sprite.set_colorkey((0,0,0))
            # sprite.blit(self.sprite_sheet,(0, 0),(0, 0, 300, 200))
            # sprite = pygame.transform.scale(sprite, (76*2,26*2))

            self.player.update(self.movement, self.map)
            self.player.render(self.screen)
            # print(self.map.map)
            self.map.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()