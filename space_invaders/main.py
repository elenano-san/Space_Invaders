import pygame
from pygame import mixer
import os
from GameClass import Game
from space_invaders.DrawingClass import Drawing
from PlayerClass import Player
from EnemyClass import Enemy

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

    player_x = ((WIDTH) - (PLAYER_IMAGE.get_width())) / 2
    player_y = 450
    player = Player(x=player_x, y=player_y, x_speed=5, y_speed=4)

    enemy_init = Enemy(speed = 3)
    enemy_wave = 4
    enemies = enemy_init.create(enemy_wave)

    draw = Drawing(WIN)
    draw.drawing(game, player, enemies, FPS=60, puntos=0)

    while run:
        clock.tick(FPS)
        
        # Game Over
        if game.over():
            if score > game.max_score:
                sound = pygame.mixer.Sound('sounds/ganar.mp3')
                sound.play()
                screen = ScreenName(score, main_menu)
                
                pygame.quit()
            else:
                main_menu()
                run = False
            continue
        
        # Cerrar juego
        if game.escape():
            run = False
            continue
        
        if len(enemies) == 0:
            game.level += 1
            enemy_wave += 1
            enemy.increase_speed()
            player.increase_speed()
            enemies = enemy.create(amount = enemy_wave)
        
        
    player.move()
    player.create_bullets()
    game.reload_bullets(len(player.bullets))
    player.cooldown()
    
    # Enemigos en movimiento
    for enemy in enemies:
        enemy.move()
        if player.hit(enemy):
            enemies.remove(enemy)
            player.fired_bullets.pop(0)
            crash_sound = pygame.mixer.Sound('sounds/explosion.wav')
            crash_sound.play()
            score += 1
        if enemy.y + enemy.get_height() > HEIGHT:
            game.lives -= 1
            enemies.remove(enemy)
            
    draw.drawing(game, player, enemies, FPS, score)
    