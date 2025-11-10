from scene import Scene
from player import Player
import pygame
import sys
from platform import Platform
from settings import *

class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player(100, HEIGHT - 100)
        self.platforms = [
            Platform(0, HEIGHT - 50, LEVEL_WIDTH, 50),
            Platform(300, 410, 200, 20),
            Platform(570, 460, 200, 20),
            Platform(640, 350, 150, 20),
            Platform(800, 300, 150, 20),
            Platform(1000, 250, 150, 20),
            Platform(1300, 200, 150, 20),
            Platform(1600, 150, 150, 20),
        ]
        self.camera_x = 0

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.handle_input()
        self.player.apply_physics(self.platforms)

        # Actualizar cámara
        self.camera_x = self.player.rect.centerx - WIDTH // 2
        self.camera_x = max(0, min(self.camera_x, 2000 - WIDTH))

    def draw(self):
        self.game.screen.fill(COLOR_BG)
        for platform in self.platforms:
            platform.draw(self.game.screen, self.camera_x)
        self.player.draw(self.game.screen, self.camera_x)
