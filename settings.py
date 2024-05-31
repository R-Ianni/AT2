import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# settings.py
class Settings:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 36)
        self.options = ["Volume", "Graphics", "Back"]
        self.selected_option = 0
        self.running = True

    def run(self):
        while self.running:
            self.window.fill((0, 0, 0))
            for index, option in enumerate(self.options):
                color = (255, 0, 0) if index == self.selected_option else (255, 255, 255)
                text = self.font.render(option, 1, color)
                self.window.blit(text, (50, 50 + index * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    return 'quit'
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected_option] == "Back":
                            return 'back'
                        else:
                            # Placeholder for setting adjustment functionality
                            print(f"Adjusting {self.options[self.selected_option]}")

            return None
