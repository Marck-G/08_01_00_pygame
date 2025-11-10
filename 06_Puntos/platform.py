import pygame
from settings import *

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, COLOR_PLATFORM,
                         pygame.Rect(self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
