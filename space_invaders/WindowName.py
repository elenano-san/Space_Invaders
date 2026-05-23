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
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Enter your name")
        self.title_font = pygame.font.Font(None, 60)
        self.subtitle_font = pygame.font.Font(None, 40)
        self.input_font = pygame.font.Font(None, 50)
        self.text_input = ''
        self.input_active = False
        self.background = self.load_images('menu_fondo.jpg')
        self.score = score

        title_text = "Congratulations! You beat the max score. Enter your name:"
        title_render = self.title_font.render(title_text, True, self.WHITE)
        title_rect = title_render.get_rect(center=(self.WIDTH / 2, 50))

        subtitle_text = "Space Invaders Hybridge"
        subtitle_render = self.subtitle_font.render(subtitle_text, True, self.WHITE)
        subtitle_rect = subtitle_render.get_rect(center=(self.WIDTH / 2, 100))

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
                    elif accept_button.collidepoint(event.pos):
                        print("Texto ingresado:", self.text_input)
                        self.escribir_en_archivo("puntajes.txt", self.text_input + "," + str(self.score))
                        finish_mtd()
                        return
                    else:
                        self.input_active = False
                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_RETURN:
                            self.escribir_en_archivo("puntajes.txt", self.text_input + "," + str(self.score))
                            finish_mtd()
                            return
                        elif event.key == pygame.K_BACKSPACE:
                            self.text_input = self.text_input[:-1]
                        else:
                            self.text_input += event.unicode

            self.window.blit(self.background, (0, 0))

            pygame.draw.rect(self.window, self.BLACK, title_rect)
            self.window.blit(title_render, title_rect)

            pygame.draw.rect(self.window, self.BLACK, subtitle_rect)
            self.window.blit(subtitle_render, subtitle_rect)

            color_input = self.GREY if not self.input_active else self.WHITE
            pygame.draw.rect(self.window, color_input, input_box, 2)
            text_surface = self.input_font.render(self.text_input, True, self.WHITE)
            self.window.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            pygame.draw.rect(self.window, self.GREY, accept_button)
            button_text = self.input_font.render("Aceptar", True, self.BLACK)
            button_text_rect = button_text.get_rect(center=accept_button.center)
            self.window.blit(button_text, button_text_rect)

            pygame.display.flip()

    def load_images(self, file_name):
        route = os.path.join('img', file_name)
        return pygame.transform.scale(pygame.image.load(route).convert(), (self.WIDTH, self.HEIGHT))

    def escribir_en_archivo(self, nombre_archivo, contenido):
        directorio_trabajo = os.getcwd()
        ruta = os.path.join(directorio_trabajo, nombre_archivo)
        try:
            if not os.path.exists(ruta):
                with open(ruta, 'w') as archivo:
                    archivo.write(contenido + '\n')
            else:
                with open(ruta, 'a') as archivo:
                    archivo.write(contenido + '\n')
        except PermissionError:
            print(f"No tiene permisos suficientes para escribir en '{os.path.dirname(ruta)}'.")
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")
