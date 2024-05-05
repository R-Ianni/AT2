import pygame
import os

# Initialize pygame
pygame.init()

# Set up the screen
# Get the absolute path of the asset directory
asset_dir = os.path.abspath("assets")

# Load images for buttons
try:
    warrior_button = pygame.image.load(os.path.join(asset_dir, "warrior_button.png"))
    mage_button = pygame.image.load(os.path.join(asset_dir, "mage_button.png"))
    rogue_button = pygame.image.load(os.path.join(asset_dir, "rogue_button.png"))
except pygame.error as e:
    print("Error loading images:", e)
    pygame.quit()
    exit()

# Set button positions
button_width = warrior_button.get_width()
button_height = warrior_button.get_height()
button_x = 400 - button_width // 2
warrior_button_y = 200
mage_button_y = 300
rogue_button_y = 400

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw buttons on the screen
    screen.blit(warrior_button, (button_x, warrior_button_y))
    screen.blit(mage_button, (button_x, mage_button_y))
    screen.blit(rogue_button, (button_x, rogue_button_y))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
