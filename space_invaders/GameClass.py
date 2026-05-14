import pygame
import os

BULLET_IMAGE = pygame.image.load(os.path.join('img', 'bullet_image.png'))

class Game:
    def __init__(self, window, screen_width, screen_height, bullets = 0, clock = pygame.time.Clock()):
        self.window = window
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.bullets = bullets
        self.clock = clock
        self.bullet_img = BULLET_IMAGE
        entries = self.read_entries("puntajes.txt")
        if len(entries) > 0:
            self.player, self.max_score = entries[0]
        else:
            self.max_score = 0
            
    def escape(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False


