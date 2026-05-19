import pygame
from pygame import mixer
import os
from GameClass import Game
from DrawingClass import Drawing
from PlayerClass import Player

#  Background
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
TITLE = 'Space Invaders Hybridge'

# Player
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

pygame.init()

# Game Window
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)
try:
    mixer.music.load('sounds/background_song.mp3')
except:
    print("No se cargó el archivo de sonido")
    pass

def main():
    puntaje = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.play(-1)
    except:
        pass

font = pygame.font.SysFont("comicsans", 60)
game = Game(font, FPS, 3, WIN, WIDTH, HEIGHT, 0, clock)

player_x = ((WIDTH) - (PLAYER_IMAGE.get_width())) / 2
player_y = 450
player = Player(x=player_x, y=player_y, x_speed=5, y_speed=4)