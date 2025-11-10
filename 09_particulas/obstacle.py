import pygame

class Obstacle:
    def __init__(self, x, y, width=44, height=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load("assets/snailShell.png")

    def draw(self, screen, camera_x):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y))