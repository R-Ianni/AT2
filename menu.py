# menu.py
import pygame
import os
import sys
from character_select import CharacterSelect
from settings import SettingsPage

class Menu:
    def __init__(self):
        # Initialise pygame
        pygame.init()

        # Set up the window
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("King's Quest")

        # Set up button colours
        self.button_background = (0, 0, 0)
        self.button_text_colour = (255, 255, 255)

        # Set up the fonts
        self.font = pygame.font.Font(None, 36)

        # Set up main menu button sizes
        self.button_width = 150
        self.button_height = 50

        # Arrange main menu buttons horizontally in the lower third
        button_y = int(self.window_height * 0.75)
        spacing = (self.window_width - (self.button_width * 3)) // 4

        self.play_button = pygame.Rect(spacing, button_y, self.button_width, self.button_height)
        self.settings_button = pygame.Rect(spacing * 2 + self.button_width, button_y, self.button_width, self.button_height)
        self.exit_button = pygame.Rect(spacing * 3 + self.button_width * 2, button_y, self.button_width, self.button_height)

        # Load the main menu background image
        asset_dir = "AT2/assets"
        try:
            self.background_image = pygame.image.load(os.path.join(asset_dir, "main_menu_background.png"))
            self.background_image = pygame.transform.smoothscale(self.background_image, (self.window_width, self.window_height))
        except Exception as e:
            print(f"Error loading main menu background image: {e}")
            sys.exit(1)

        # Initialise the character select and settings pages
        self.character_select = CharacterSelect(self.window, self.font, self.background_image)
        self.settings_page = SettingsPage(self.window, self.font, self.background_image)

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
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.play_button.collidepoint(mouse_x, mouse_y):
                        # Switch to character selection screen
                        self.character_select.run()
                    elif self.settings_button.collidepoint(mouse_x, mouse_y):
                        # Switch to settings page
                        self.settings_page.run()
                    elif self.exit_button.collidepoint(mouse_x, mouse_y):
                        pygame.quit()
                        sys.exit()

            self.window.blit(self.background_image, (0, 0))

            self.draw_button(self.play_button, "Play")
            self.draw_button(self.settings_button, "Settings")
            self.draw_button(self.exit_button, "Exit")

            pygame.display.flip()

# Create an instance of the Menu class and run the menu
menu = Menu()
menu.run()
