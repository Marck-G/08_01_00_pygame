import pygame, sys
from scene import Scene
from game_scene import GameScene
from settings import *

class GameOverScene(Scene):
    def __init__(self, game, score):
        super().__init__(game)
        self.score = score
        self.font = pygame.font.SysFont(None, 60)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_scene(GameScene(self.game))

    def update(self):
        pass

    def draw(self):
        self.game.screen.fill((150, 0, 0))
        text1 = self.font.render(f"GAME OVER", True, (255, 255, 255))
        text2 = self.font.render(f"Puntos: {self.score}", True, (255, 255, 0))
        text3 = self.font.render("PULSE ENTER PARA REINTENTAR", True, (255, 255, 255))
        self.game.screen.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//3))
        self.game.screen.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2))
        self.game.screen.blit(text3, (WIDTH//2 - text3.get_width()//2, HEIGHT//1.5))
