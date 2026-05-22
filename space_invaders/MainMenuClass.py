import pygame
import os
from pygame import mixer

pygame.init()

class MainMenu:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    
    # Tamaño de la pantalla
    WIDTH = 800
    HEIGHT = 600
    
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders Elenano")
    try:
        mixer.music.load('sounds/background_song.mp3')
        
    except:
        print("No se pudo reproducir el archivo de sonido")
        pass
    try:
        mixer.music.play(-1)
    except:
        pass
    
    DIR_IMAGES = 'img'
    def __init__(self, init_game_mtd, init_score_mtd, init_about_mtd):
        self.init_game_mtd = init_game_mtd
        self.init_score_mtd = init_score_mtd
        self.init_about_mtd = init_about_mtd
        
    # Cargar imágenes
    def load_images(self, file_name):
        route = os.path.join(self.DIR_IMAGES, file_name)
        return pygame.image.load(route).convert_alpha()
    
    def show_text(self, text, font, color, x, y):
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_object, text_rect)