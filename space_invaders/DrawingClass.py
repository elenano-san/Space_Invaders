import pygame
import os

current_dir = os.path.dirname(__file__)
BACKGROUND = pygame.image.load(os.path.join(current_dir, 'img', 'background.png'))
HEIGHT = 600


class Drawing:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("comicsans", 40)

    def drawing(self, game, player, enemies, score):
        self.window.blit(BACKGROUND, (0, 0))
        player.fire(self.window)

        for enemy in enemies[:]:
            enemy.draw(self.window)

        player.draw(self.window)

        game.draw_HUD()
        points_label = self.font.render(f'Score: {score}', 1, (255, 255, 255))
        self.window.blit(points_label, (10, HEIGHT - 40))
        pygame.display.update()
