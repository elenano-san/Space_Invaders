import pygame
import os
from pygame import mixer


class MainMenu:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)

    WIDTH = 800
    HEIGHT = 600
    DIR_IMAGES = 'img'

    def __init__(self, init_game_mtd, init_score_mtd, init_about_mtd):
        self.init_game_mtd = init_game_mtd
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Space Invaders Elenano")
        try:
            mixer.music.load('sounds/background_song.mp3')
        except:
            print("No se pudo reproducir el archivo de sonido")
        try:
            mixer.music.play(-1)
        except:
            pass

    def load_images(self, file_name):
        route = os.path.join(self.DIR_IMAGES, file_name)
        return pygame.image.load(route).convert_alpha()

    def show_text(self, text, font, color, x, y):
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        self.window.blit(text_object, text_rect)
        return text_rect

    def main_menu(self):
        options = ["Start Game", "High Scores", "About"]
        option_output = 0
        selector_rect = pygame.Rect(0, 0, 300, 50)

        background = self.load_images('menu_fondo.jpg')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))

        image = self.load_images('hybridge.gif')
        image = pygame.transform.scale(image, (80, 80))

        while True:
            self.window.blit(background, (0, 0))
            self.show_text("Space Invaders", pygame.font.Font(None, 60), self.WHITE, self.WIDTH / 2, self.HEIGHT / 4)
            self.show_text("Elenano", pygame.font.Font(None, 60), self.WHITE, self.WIDTH / 2, self.HEIGHT / 4 + 60)

            rectangles_text = []
            for i, option in enumerate(options):
                rect_text = self.show_text(option, pygame.font.Font(None, 40), self.WHITE,
                                           self.WIDTH / 2, self.HEIGHT / 4 + 90 * (i + 1) + 100)
                rectangles_text.append(rect_text)

            selector_rect.centerx = self.WIDTH / 2
            selector_rect.centery = rectangles_text[option_output].centery

            pygame.draw.rect(self.window, self.RED, selector_rect, 2)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        option_output = (option_output - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        option_output = (option_output + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        option_selected = options[option_output]

                        if option_selected.lower() == "start game":
                            self.init_game_mtd()
                        elif option_selected.lower() == "high scores":
                            self.init_score_mtd()
                        elif option_selected.lower() == "about":
                            self.init_about_mtd()
                        else:
                            print("Opción no válida")
