import pygame
import random
from settings import *

class Enemy:
    def __init__(self, x, y, speed=2):
        self.rect = pygame.Rect(x, y, 71, 36)  # Tamaño del sprite
        self.speed = speed
        # random initial direction
        self.direction = random.choice([-1, 1])
        # frames para animación (placeholder)
        self.frames = [
            pygame.image.load("assets/flyFly1.png"),
            pygame.image.load("assets/flyFly2.png")
        ]
        self.frame_index = 0
        self.animation_timer = 0

    def update(self):
        # Movimiento horizontal simple
        self.rect.x += self.speed * self.direction

        # Cambiar dirección al tocar límites (ejemplo fijo)
        if self.rect.x < 0 or self.rect.x + self.rect.width > LEVEL_WIDTH:
            self.direction *= -1
        # Actualizar animación
        self.animation_timer += 1
        if self.animation_timer >= 20:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def draw(self, screen, camera_x):
        screen.blit(self.frames[self.frame_index], (self.rect.x - camera_x, self.rect.y))
