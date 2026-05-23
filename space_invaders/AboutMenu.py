import pygame
import sys
import os
import webbrowser

# Definir la clase AboutMenu
class AboutMenu:
    # Definir colores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    RED = (255, 0, 0)
    
    # Configurar la ventana
    WIDTH = 800
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("About")
    
    def __init__(self, back_mtd):
        self.back_mtd = back_mtd
        
        # Función para cargar imágenes
        def load_images(self, file_name):
            route = os.path.join('img', file_name)
            return pygame.image.load(route).convert_alpha()
        
        # Función para mostrar texto en la pantalla
        def show_text(self, text, font, color, surface, x, y):
            text_object = font.render(text, True, color)
            text_rect = text_object.get_rect()
            text_rect.topleft = (x, y)
            surface.blit(text_object, text_rect)
            
        # Función para dibujar un botón
        def draw_button(self, text, font, color, surface, x, y, width, height):
            pygame.draw.rect(surface, color, (x, y, width, height))
            text_width, text_height = font.size(text)
            text_x = x + (width - text_width) // 2
            text_y = y + (height - text_height) // 2
            self.show_text(text, font, self.BLACK, surface, text_x, text_y)
            
        # Funcion para mostrar el contenito
        def show_content(self, content, content_font, y_offset):
            available_horizontal_space = self.WIDTH - 100
            for line in content.split('\n'):
                words = line.split(' ')
                text_line = ''
                for word in words:
                    text_line_temp = text_line + word + ' '
                    text_width_temp = font_content.size(text_line_temp)[0]
                    if text_width_temp < available_horizontal_space:
                        text_line = text_line_temp
                    else:
                        self.show_text(text_line.strip(), font_content, self.WHITE, self.window, (self.WIDTH - font_content.size(text_line.strip())[0]) // 2, y_offset)
                        y_offset += font_content.size(text_line.strip())[1]
                        
        # Función para mostrar el menú Acerca de
        def show_menu(self):
            self.window.fill(self.BLACK)
            
            # Cargar imagen de fondo
            background = self.load_images('menu_fondo.jpg')
            background = pygame.transform.scale(background, (self.WIDTH, self.HEIGHT))
            self.window.blit(background, (0, 0))
            
            # Mostrar título
            title_text = "About"
            title_font = pygame.font.Font(None, 48)
            title_width = title_font-size(title_text)[0]
            title_x = (self.WIDTH - title_width) // 2
            self.show_text(title_text, title_font, self.WHITE, self.window, title_x, 50)
            
            # Show subtitle
            subtitle_text = "Space Invaders Elenano"
            subtitle_font = pygame.font.Font(None, 36)
            subtitle_width = subtitle_font.size(subtitle_text)[0]
            subtitle_x = (self.WIDTH - subtitle_width) // 2
            self.show_text(subtitle_text, subtitle_font, self.WHITE, self.window, subtitle_x, 120)
            
            # Show content
            content = "This game was developed by Elenano as a project for the Hybridge course. It is a remake of the classic Space Invaders game, where players control a spaceship and must defend against waves of alien invaders. The game features multiple levels, power-ups, and a high score system. We hope you enjoy playing it as much as we enjoyed creating it!"
            font_content = pygame.font.Font(None, 24)
            y_offset = max(200, subtitle_font.size(subtitle_text)[1] + 120)
            self.show_content(content, font_content, y_offset)
            
            # Mostrar texto de enlace
            link_text = "Visit Hybridge website"
            link_font = pygame.font.Font(None, 28)
            link_width = link_font.size(link_text)[0]
            link_x = (self.WIDTH - link_width) // 2
            self.show_text(link_text, link_font, self.RED, self.window, 20, 20, 50, 50)
            pygame.display.update()
            
        # Función principal para ejecutar el menú Acerca de
        def execute(self):
            self.show_menu()
            
            # Bucle principal del menú
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # Left mouse button
                            x, y = event.pos
                            if 20 <= x <= 70 and 20 <= y <= 50:  # Coordenadas para el botón atrás
                                print("Back button clicked")
                                self.back_mtd()
                                pygame.quit()
                                
                            elif 300 <= y <= 520: # Coordenadas para el texto de enlace
                                webbrowser.open("https://hybridge.education/")
                                    
# Inicializar Pygame
pygame.init()