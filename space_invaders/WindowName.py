import pygame
import sys
import os

class WindowName:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (200, 200, 200)
    
    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self, score, finish_mtd):
        pygame.init()
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Enter your name")
        self.title_font = pygame.font.Font(None, 60)
        self.subtitle_font = pygame.font.Font(None, 40)
        self.input_font = pygame.font.Font(None, 50)
        self.text_input = ''
        self.input_font
        self.background = self.load_images('menu_fondo.jpg')
        self.score = score
        
        
        title_text = "Congratulations! You have beaten the max score. Please enter your name: "
        title_render = self.title_font.render(title_text, True, self.WHITE)
        title_rect = title_render.get_rect(center=(self.WIDTH/2, 50))
        
        subtitle_text = "Space Invaders Hybridge"
        subtitle_render = self.subtitle_font.render(subtitle_text, True, self.WHITE)
        subtitle_rect = subtitle_render.get_rect(center=(self.WIDTH/2, 100))
        
        input_box = pygame.Rect(200, 200, 400, 50)
        
        accept_button = pygame.Rect(300, 300, 200, 50)
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        self.input_active = not self.input_active
                    else:
                        self.input_active = False
                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_RETURN:
                            print(self.texto_input)
                            self.texto_input = ""
                        elif event.key == pygame.K_BACKSPACE:
                            self.texto_input = self.texto_input[:-1]
                        else:
                            self.texto_input += event.unicode
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if accept_button.collidepoint(event.pos):
                        print("Texto ingresado:", self.texto_input)
                        self.escribir_en_archivo("puntajes.txt", self.texto_input+","+str(self.puntaje))
                        finish_mtd()
                        pygame.quit()

            self.ventana.blit(self.fondo, (0, 0))

            pygame.draw.rect(self.ventana, self.NEGRO, title_rect)
            self.ventana.blit(title_render, title_rect)

            pygame.draw.rect(self.ventana, self.NEGRO, subtitle_rect)
            self.ventana.blit(subtitle_render, subtitle_rect)

            color_input = self.GRIS if not self.input_active else self.BLANCO
            pygame.draw.rect(self.ventana, color_input, input_box, 2)
            texto_superficie = self.fuente_input.render(self.texto_input, True, self.BLANCO)
            self.ventana.blit(texto_superficie, (input_box.x + 5, input_box.y + 5))

            pygame.draw.rect(self.ventana, self.GRIS, accept_button)
            texto_boton = self.fuente_input.render("Aceptar", True, self.NEGRO)
            texto_boton_rect = texto_boton.get_rect(center=accept_button.center)
            self.ventana.blit(texto_boton, texto_boton_rect)

            pygame.display.flip()

    def cargar_imagen(self, nombre_archivo):
            ruta = "img/" + nombre_archivo
            return pygame.transform.scale(pygame.image.load(ruta).convert(), (self.ANCHO, self.ALTO))
    
    def escribir_en_archivo(self, nombre_archivo, contenido):
        directorio_trabajo = os.getcwd()
        ruta = os.path.join(directorio_trabajo, nombre_archivo)
        try:
            if not os.path.exists(ruta):
                with open(ruta,'w') as archivo:
                    archivo.write(contenido + '\n')
                    print(f"Se ha creado el archivo '{ruta}' y se ha escrito el contenido.")
            else:
                print(f"El archivo '{ruta}' ya existe.")
                with open(ruta, 'a') as archivo:
                    archivo.write(contenido + '\n')

        except PermissionError:
            print(f"No tiene permisos suficientes para escribir en el directorio '{os.path.dirname(ruta)}'.")
        except Exception as e:
            print(f"Error al crear o escribir en el archivo: {e}")

def finish():
    print("terminado")