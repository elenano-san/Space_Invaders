import pygame
import sys
import os


class ScoreMenu:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("High Scores")

    def load_scores(self, filename):
        scores = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, score = line.strip().split(',')
                    scores.append((name, int(score)))
        except FileNotFoundError:
            print(f"No se encontró el archivo {filename}.")
        return sorted(scores, key=lambda x: x[1], reverse=True)[:5]

    def load_images(self, file_name):
        route = os.path.join('img', file_name)
        return pygame.image.load(route).convert_alpha()

    def show_text(self, text, font, color, surface, x, y):
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_object, text_rect)

    def draw_button(self, text, font, color, surface, x, y, width, height):
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.show_text(text, font, self.BLACK, surface, x + width // 2, y + height // 2)

    def show_scores(self, scores):
        self.window.fill(self.BLACK)

        background = self.load_images('menu_fondo.jpg')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.window.blit(background, (0, 0))

        self.show_text("High Scores", pygame.font.Font(None, 60), self.WHITE, self.window, self.WIDTH // 2, 50)
        self.show_text("Space Invaders", pygame.font.Font(None, 36), self.WHITE, self.window, self.WIDTH // 2, 120)

        if not scores:
            self.show_text("No scores available", pygame.font.Font(None, 36), self.RED,
                           self.window, self.WIDTH // 2, self.HEIGHT // 2)
        else:
            y_offset = 250
            for i, (name, score) in enumerate(scores, 1):
                text_color = self.WHITE if i == 1 else self.RED
                font_size = 42 if i == 1 else 36
                self.show_text(f"{i}. {name}: {score}", pygame.font.Font(None, font_size),
                               text_color, self.window, self.WIDTH // 2, y_offset)
                y_offset += 60

        self.draw_button("<", pygame.font.Font(None, 30), self.GREY, self.window, 20, 20, 50, 50)
        pygame.display.update()

    def execute(self):
        scores = self.load_scores("puntajes.txt")
        self.show_scores(scores)

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
