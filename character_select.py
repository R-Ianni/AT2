# character_select.py
import pygame
import os
import sys

class CharacterSelect:
    def __init__(self, window, font, background_image):
        self.window = window
        self.font = font
        self.background_image = background_image

        # Set up button colours
        self.button_background = (0, 0, 0)
        self.button_text_colour = (255, 255, 255)

        # Load character images
        asset_dir = "AT2/assets"
        self.warrior_button = pygame.image.load(os.path.join(asset_dir, "warrior_button.png"))
        self.mage_button = pygame.image.load(os.path.join(asset_dir, "mage_button.png"))
        self.rogue_button = pygame.image.load(os.path.join(asset_dir, "rogue_button.png"))

        # Scale character selection buttons to fit the screen
        self.character_button_width = window.get_width() // 3
        self.character_button_height = int(window.get_height() * 0.5)

        self.warrior_button = pygame.transform.smoothscale(self.warrior_button, (self.character_button_width, self.character_button_height))
        self.mage_button = pygame.transform.smoothscale(self.mage_button, (self.character_button_width, self.character_button_height))
        self.rogue_button = pygame.transform.smoothscale(self.rogue_button, (self.character_button_width, self.character_button_height))

        # Arrange character selection buttons horizontally
        self.button_spacing = (window.get_width() - (self.character_button_width * 3)) // 4
        self.warrior_rect = pygame.Rect(self.button_spacing, 50, self.character_button_width, self.character_button_height)
        self.mage_rect = pygame.Rect(self.character_button_width + self.button_spacing * 2, 50, self.character_button_width, self.character_button_height)
        self.rogue_rect = pygame.Rect(self.character_button_width * 2 + self.button_spacing * 3, 50, self.character_button_width, self.character_button_height)

        # Set up the back button
        self.back_button = pygame.Rect(350, 500, 100, 50)

    def draw_button(self, rect, label):
        pygame.draw.rect(self.window, self.button_background, rect)
        text = self.font.render(label, True, self.button_text_colour)
        text_rect = text.get_rect(center=rect.center)
        self.window.blit(text, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.warrior_rect.collidepoint(mouse_x, mouse_y):
                        print("Warrior button clicked")
                    elif self.mage_rect.collidepoint(mouse_x, mouse_y):
                        print("Mage button clicked")
                    elif self.rogue_rect.collidepoint(mouse_x, mouse_y):
                        print("Rogue button clicked")
                    elif self.back_button.collidepoint(mouse_x, mouse_y):
                        return

            self.window.blit(self.background_image, (0, 0))

            self.window.blit(self.warrior_button, self.warrior_rect)
            self.window.blit(self.mage_button, self.mage_rect)
            self.window.blit(self.rogue_button, self.rogue_rect)

            self.draw_button(self.back_button, "Back")
            pygame.display.flip()
