import pygame
from settings import *
from particle import Particle

class Coin:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 70, 70)
        self.collected = False
        self.image = pygame.image.load("assets/coinGold.png")
        self.particles = []
        self.sound = pygame.mixer.Sound("assets/Rise06.mp3")
        self.sound.set_volume(0.6)
    def collect(self):
        self.collected = True
        self.sound.play()
        # Generar partículas doradas
        for _ in range(10):
            self.particles.append(Particle(self.rect.centerx, self.rect.centery, (255, 215, 0)))

    def update(self):
        for p in self.particles[:]:
            p.update()
            if p.lifetime <= 0:
                self.particles.remove(p)

    def draw(self, screen, camera_x):
        if not self.collected:
            screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))
        for p in self.particles:
            p.draw(screen, camera_x)
