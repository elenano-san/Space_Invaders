import pygame
import sys
import os

# Definir la clase MenuPuntajes
class ScoreMenu:
    # Definir colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)
    
    # Configurar la ventana
    WIDTH = 800
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("High Scores")
    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
    # Función para cargar puntajes desde un archivo de texto
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
    
    # Función para cargar imágenes
    def load_images(self, file_name):
        route = os.path.join('img', file_name)
        return pygame.image.load(route).convert_alpha()
    
    # Función para mostrar texto en la pantalla
    def show_text(self, text, font, color, surface, x, y):
        text_object = font.render(text, True, color)
        text_rect = text_object.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_object, text_rect)
        
    # Función para dibujar un botón
    def draw_button(self, text, font, color, surface, x, y, width, height):
        pygame.draw.rect(surface, color, (x, y, width, height))
        self.show_text(text, font, self.BLACK, surface, x + width // 2, y + height // 2)
        
    # Función para mostrar los mejores puntajes en la pantalla
    def show_scores(self, scores):
        self.window.fill(self.BLACK)
        
        # Cargar imagen de fondo
        background = self.load_images('menu_fondo.jpg')
        background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
        self.window.blit(background, (0, 0))
        
        # Mostrar título
        self.show_text("High Scores", pygame.font.Font(None, 60), self.WHITE, self.window, self.WIDTH // 2, 50)
        
        # Mostrar subtítulo de juego
        self.show_text("Space Invaders", pygame.font.Font(None, 36), self.WHITE, self.window, self.WIDTH // 2, 120)
        
        if not scores:
            self.show_text("No scores available", pygame.font.Font(None, 36), self.RED, self.window, self.WIDTH // 2, self.HEIGHT // 2)
        else:
            # Mostrar cada puntaje
            y_offset = 250
            for i, (name, score) in enumerate(scores, 1):
                text_color = self.WHITE if i == 1 else self.RED
                font_size = 42 if i == 1 else 36 # Tamaño de fuente más grande para el primer lugar
                self.show_text(f"{i}. {name}: {score}", pygame.font.Font(None, font_size), text_color, self.window, self.WIDTH // 2, y_offset)
                y_offset += 60
                
        # Dibujar botón de regreso
        self.draw_button("<", pygame.font.Font(None, 30), self.GREY, self.window, 20, 20, 50, 50)
        
        pygame.display.update()
        
    # Función principal para ejecutar la pantalla de puntajes
    def execute(self):
        scores = self.load_scores("puntajes.txt") # Nombre del archivo de puntajes
        self.show_scores(scores)
        
        # Bucle principal para manejar eventos
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Click izquierdo
                        x, y = event.pos
                        if 20 <= x <= 70 and 20 <= y <= 70: # Verificar si se hizo click en el botón de regreso
                            print("Acción atrás")
                            self.back_mtd() # Llamar a la función para regresar al menú principal
                            pygame.quit()
                            
# Inicializar pygame
pygame.init()
