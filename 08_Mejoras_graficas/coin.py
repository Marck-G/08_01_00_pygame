import pygame
from settings import *

class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 70, 70)
        self.collected = False
        self.image = pygame.image.load("assets/coinGold.png")

    def draw(self, screen, camera_x):
        if not self.collected:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
