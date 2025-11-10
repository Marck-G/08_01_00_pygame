import pygame
import sys
from scene import Scene
from game_scene import GameScene
from settings import *

class MenuScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont(None, 60)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.game.change_scene(GameScene(self.game))

    def update(self):
        pass

    def draw(self):
        self.game.screen.fill((50, 50, 100))
        text = self.font.render("PULSE ENTER PARA JUGAR", True, (255, 255, 255))
        self.game.screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
