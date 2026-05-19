from EnemyClass import HEIGHT
from EnemyClass import WIDTH
from main import BACKGROUND
import pygame
import os
from enemyClass import Enemy
from ShipClass import Ship
from GameClass import Game
from BulletClass import Bullet

current_dir = os.path.dirname(__file__)
BACKGROUND = pygame.image.load(os.path.join('img', 'background.png'))
WIDTH, HEIGHT = 800, 600

class Drawing:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("comicsans", 60)
        
    def drawing(self, ship, enemies, bullets, player):
        self.window.blit(BACKGROUND, (0, 0))
        player.fire(self.window)
        
        for enemy in enemies[:]:
            enemy.draw(self.window)
            
        player.draw(self.window)
        
    game.draw_HUD()
    points_label = self.font.render(f'Score: {score}', 1, (255,255,255))
    self.window.blit(points_label, (HEIGHT/2, 10))
    pygame.display.update()
    