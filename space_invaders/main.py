import pygame
from pygame import mixer
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

from GameClass import Game
from PlayerClass import Player
from EnemyClass import Enemy
from DrawingClass import Drawing
from MainMenuClass import MainMenu
from MenuPuntajesClass import ScoreMenu
from AboutMenu import AboutMenu
from WindowName import WindowName

BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
ICON_IMAGE = pygame.image.load(os.path.join('img', 'title_icon.png'))
PLAYER_IMAGE = pygame.image.load(os.path.join('img', 'player_image.png'))
TITLE = 'Space Invaders Hybridge'

pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON_IMAGE)

try:
    mixer.music.load('sounds/background_song.mp3')
except:
    print("No se cargó el archivo de sonido")

def main():
    score = 0
    run = True
    clock = pygame.time.Clock()
    FPS = 60
    try:
        mixer.music.play(-1)
    except:
        pass

    font = pygame.font.SysFont("comicsans", 60)
    game = Game(font, FPS, 3, WIN, WIDTH, HEIGHT, 0, clock)

    player_x = (WIDTH - PLAYER_IMAGE.get_width()) / 2
    player_y = 450
    player = Player(x=player_x, y=player_y, x_speed=5, y_speed=4)

    enemy = Enemy(speed=3)
    enemy_wave = 4
    enemies = enemy.create(enemy_wave)

    draw = Drawing(WIN)

    while run:
        clock.tick(FPS)

        if game.over():
            if score > game.max_score:
                sound = pygame.mixer.Sound('sounds/ganar.mp3')
                sound.play()
                WindowName(score, main_menu)
            else:
                main_menu()
            run = False
            continue

        if game.escape():
            run = False
            continue

        if len(enemies) == 0:
            game.level += 1
            enemy_wave += 1
            enemy.increase_speed()
            player.increase_speed()
            enemies = enemy.create(amount=enemy_wave)

        player.move()
        player.create_bullets()
        game.reload_bullet(len(player.bullets))
        player.cooldown()

        for enemy_obj in enemies[:]:
            enemy_obj.move()
            if player.hit(enemy_obj):
                enemies.remove(enemy_obj)
                if player.fired_bullets:
                    player.fired_bullets.pop(0)
                crash_sound = pygame.mixer.Sound('sounds/explosion.wav')
                crash_sound.play()
                score += 1
            elif enemy_obj.y + enemy_obj.get_height() > HEIGHT:
                game.lives -= 1
                enemies.remove(enemy_obj)

        draw.drawing(game, player, enemies, score)

def init_game():
    main()

def init_score():
    ScoreMenu(main_menu).execute()

def init_about():
    AboutMenu(main_menu).execute()

def main_menu():
    MainMenu(init_game, init_score, init_about).main_menu()

main_menu()
