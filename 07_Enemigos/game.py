import pygame
from settings import *
from menu_scene import MenuScene

class Game:
    def __init__(self):
        pygame.init()
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
