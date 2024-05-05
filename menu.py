import pygame
import sys
pygame.init()

# Set up the buttons
play_button = pygame.Rect(300, 200, 200, 50)
settings_button = pygame.Rect(300, 300, 200, 50)
exit_button = pygame.Rect(300, 400, 200, 50)

# Character select screen
def character_select():
    # Add your code here to implement the character select screen
    print("Character select screen")

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                # Handle play button click
                character_select()  # Open character select screen
            if settings_button.collidepoint(mouse_pos):
                # Handle settings button click
                print("Settings button clicked")
            if exit_button.collidepoint(mouse_pos):
                # Handle exit button click
                pygame.quit()
                sys.exit()
    # Set up the window
    window_width = 800

    # Rest of the code...

    # Game loop
    while True:
        # Handle events
        window_height = 600
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("RPG Game")

        # Set up the colors
        background_color = (0, 0, 0)
        button_color = (255, 255, 255)

        # Set up the fonts
        font = pygame.font.Font(None, 36)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if play_button.collidepoint(mouse_pos):
                    # Handle play button click
                    print("Play button clicked")

                if settings_button.collidepoint(mouse_pos):
                    # Handle settings button click
                    print("Settings button clicked")

                if exit_button.collidepoint(mouse_pos):
                    # Handle exit button click
                    pygame.quit()
                    sys.exit()

        # Clear the screen
        window.fill(background_color)

        # Draw the buttons
        pygame.draw.rect(window, button_color, play_button)
        pygame.draw.rect(window, button_color, settings_button)
        pygame.draw.rect(window, button_color, exit_button)

        # Draw the button labels
        play_text = font.render("Play", True, (0, 0, 0))
        window.blit(play_text, (350, 210))

        settings_text = font.render("Settings", True, (0, 0, 0))
        window.blit(settings_text, (330, 310))

        exit_text = font.render("Exit", True, (0, 0, 0))
        window.blit(exit_text, (360, 410))

        # Update the display
        pygame.display.flip()
# Quit the game