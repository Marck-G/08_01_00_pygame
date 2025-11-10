import pygame
from settings import *
from menu_scene import MenuScene

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # Inicializa el sistema de sonido

        # Música de fondo
        pygame.mixer.music.load("assets/background.mp3")
        pygame.mixer.music.set_volume(0.3)  # Volumen 0.0 a 1.0
        pygame.mixer.music.play(-1)  # Loop infinito
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego de Plataformas - Escenas")
        self.clock = pygame.time.Clock()
        self.scene = MenuScene(self)  # Empezamos en el menú

    def change_scene(self, scene):
        self.scene = scene

    def run(self):
        while True:
            events = pygame.event.get()
            self.scene.handle_events(events)
            self.scene.update()
            self.scene.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
