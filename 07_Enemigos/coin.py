import pygame
from settings import *

class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.collected = False

    def draw(self, screen, camera_x):
        if not self.collected:
            pygame.draw.rect(screen, (255, 215, 0), 
                             pygame.Rect(self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
