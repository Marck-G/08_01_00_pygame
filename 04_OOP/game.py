import pygame, sys
from settings import *
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Juego de Plataformas - OOP")
        self.clock = pygame.time.Clock()

        self.player = Player(100, HEIGHT - 100)
        self.platforms = self.create_platforms()
        self.camera_x = 0

    def create_platforms(self):
        return [
            Platform(0, HEIGHT - 50, LEVEL_WIDTH, 50),
            Platform(300, 410, 200, 20),
            Platform(570, 460, 200, 20),
            # Platform(520, 400, 200, 20),
            Platform(640, 350, 150, 20),
            Platform(800, 300, 150, 20),
            Platform(1000, 250, 150, 20),
            Platform(1300, 200, 150, 20),
            Platform(1600, 150, 150, 20),
        ]

    def run(self):
        """Main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.player.handle_input()
            self.player.apply_physics(self.platforms)

            # Cámara
            self.camera_x = self.player.rect.centerx - WIDTH // 2
            self.camera_x = max(0, min(self.camera_x, LEVEL_WIDTH - WIDTH))

            # Dibujar
            self.screen.fill(COLOR_BG)
            for platform in self.platforms:
                platform.draw(self.screen, self.camera_x)
            self.player.draw(self.screen, self.camera_x)

            pygame.display.flip()
            self.clock.tick(FPS)
