from scene import Scene
from player import Player
import pygame
import sys
from platform import Platform
from settings import *
from coin import Coin

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
        self.coins = [Coin(350, 470), Coin(850, 230), Coin(1350, 70)]
        self.score = 0
        self.lives = 3
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

        # Verificar colisiones con monedas
        for coin in self.coins:
            if not coin.collected and self.player.rect.colliderect(coin.rect):
                coin.collected = True
                self.score += 10
        if self.player.rect.top > HEIGHT:
            self.lives -= 1
            if self.lives <= 0:
                from game_over import GameOverScene
                self.game.change_scene(GameOverScene(self.game, self.score))
            else:
                # Reiniciar jugador en inicio
                self.player.rect.topleft = (100, HEIGHT - 100)
                self.player.vel_y = 0

    def draw(self):
        self.game.screen.fill(COLOR_BG)
        for platform in self.platforms:
            platform.draw(self.game.screen, self.camera_x)
        for coin in self.coins:
            coin.draw(self.game.screen, self.camera_x)
        self.player.draw(self.game.screen, self.camera_x)

        # Mostrar puntuación y vidas
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Puntos: {self.score}", True, (255, 255, 255))
        lives_text = font.render(f"Vidas: {self.lives}", True, (255, 0, 0))
        self.game.screen.blit(score_text, (10, 10))
        self.game.screen.blit(lives_text, (10, 40))
