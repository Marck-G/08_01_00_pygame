import pygame
import random

class Particle:
    def __init__(self, x, y, color, lifetime=20):
        self.x = x
        self.y = y
        self.color = color
        self.lifetime = lifetime
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-3, 0)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += 0.1  # gravedad ligera
        self.lifetime -= 1

    def draw(self, screen, camera_x):
        pygame.draw.circle(screen, self.color, (int(self.x - camera_x), int(self.y)), 3)
