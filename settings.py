# settings_page.py
import pygame
import sys

class SettingsPage:
    def __init__(self, window, font, background_image):
        self.window = window
        self.font = font
        self.background_image = background_image

        # Button colours
        self.button_background = (0, 0, 0)
        self.button_text_colour = (255, 255, 255)

        # Set up the buttons
        self.music_button = pygame.Rect(325, 200, 150, 50)
        self.controls_button = pygame.Rect(325, 300, 150, 50)
        self.graphics_button = pygame.Rect(325, 400, 150, 50)
        self.back_button = pygame.Rect(325, 500, 150, 50)

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
                    if self.music_button.collidepoint(mouse_x, mouse_y):
                        print("Music settings clicked")
                    elif self.controls_button.collidepoint(mouse_x, mouse_y):
                        print("Controls settings clicked")
                    elif self.graphics_button.collidepoint(mouse_x, mouse_y):
                        print("Graphics settings clicked")
                    elif self.back_button.collidepoint(mouse_x, mouse_y):
                        return

            self.window.blit(self.background_image, (0, 0))

            self.draw_button(self.music_button, "Music")
            self.draw_button(self.controls_button, "Controls")
            self.draw_button(self.graphics_button, "Graphics")
            self.draw_button(self.back_button, "Back")

            pygame.display.flip()
