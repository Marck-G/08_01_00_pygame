import pygame
from settings import *

class Enemy:
    def __init__(self, x, y, width=50, height=50, speed=2):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.direction = 1  # 1 = derecha, -1 = izquierda

    def update(self):
        # Movimiento horizontal simple
        self.rect.x += self.speed * self.direction

        # Cambiar dirección al tocar límites (ejemplo fijo)
        if self.rect.x < 0 or self.rect.x + self.rect.width > LEVEL_WIDTH:
            self.direction *= -1

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, (200, 0, 0),
                         pygame.Rect(self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
