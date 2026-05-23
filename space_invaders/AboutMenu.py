import pygame
import sys
import os
import webbrowser


class AboutMenu:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("About")

    def load_images(self, file_name):
        route = os.path.join('img', file_name)
        return pygame.image.load(route).convert_alpha()

    def show_text(self, text, font, color, x, y):
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.topleft = (x, y)
        self.window.blit(text_object, text_rect)

    def draw_button(self, text, font, color, x, y, width, height):
        pygame.draw.rect(self.window, color, (x, y, width, height))
        text_width, text_height = font.size(text)
        text_x = x + (width - text_width) // 2
        text_y = y + (height - text_height) // 2
        self.show_text(text, font, self.BLACK, text_x, text_y)

    def show_content(self, content, font_content, y_offset):
        available_horizontal_space = self.WIDTH - 100
        for line in content.split('\n'):
            words = line.split(' ')
            text_line = ''
            for word in words:
                text_line_temp = text_line + word + ' '
                text_width_temp = font_content.size(text_line_temp)[0]
                if text_width_temp < available_horizontal_space:
                    text_line = text_line_temp
                else:
                    x = (self.WIDTH - font_content.size(text_line.strip())[0]) // 2
                    self.show_text(text_line.strip(), font_content, self.WHITE, x, y_offset)
                    y_offset += font_content.size(text_line.strip())[1]
                    text_line = word + ' '
            if text_line.strip():
                x = (self.WIDTH - font_content.size(text_line.strip())[0]) // 2
                self.show_text(text_line.strip(), font_content, self.WHITE, x, y_offset)
                y_offset += font_content.size(text_line.strip())[1]

    def show_menu(self):
        self.window.fill(self.BLACK)

        background = self.load_images('menu_fondo.jpg')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.window.blit(background, (0, 0))

        title_text = "About"
        title_font = pygame.font.Font(None, 48)
        title_width = title_font.size(title_text)[0]
        title_x = (self.WIDTH - title_width) // 2
        self.show_text(title_text, title_font, self.WHITE, title_x, 50)

        subtitle_text = "Space Invaders Elenano"
        subtitle_font = pygame.font.Font(None, 36)
        subtitle_width = subtitle_font.size(subtitle_text)[0]
        subtitle_x = (self.WIDTH - subtitle_width) // 2
        self.show_text(subtitle_text, subtitle_font, self.WHITE, subtitle_x, 120)

        content = ("This game was developed by Elenano as a project for the Hybridge course. "
                   "It is a remake of the classic Space Invaders game, where players control a spaceship "
                   "and must defend against waves of alien invaders. The game features multiple levels, "
                   "power-ups, and a high score system. We hope you enjoy playing it as much as we enjoyed creating it!")
        font_content = pygame.font.Font(None, 24)
        y_offset = max(200, subtitle_font.size(subtitle_text)[1] + 120)
        self.show_content(content, font_content, y_offset)

        link_text = "Visit Hybridge website"
        link_font = pygame.font.Font(None, 28)
        link_width = link_font.size(link_text)[0]
        link_x = (self.WIDTH - link_width) // 2
        self.show_text(link_text, link_font, self.RED, link_x, self.HEIGHT - 80)

        self.draw_button("<", pygame.font.Font(None, 30), self.GREY, 20, 20, 50, 50)
        pygame.display.update()

    def execute(self):
        self.show_menu()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70:
                            self.back_mtd()
                            return
                        elif self.HEIGHT - 80 <= y <= self.HEIGHT - 50:
                            webbrowser.open("https://hybridge.education/")
