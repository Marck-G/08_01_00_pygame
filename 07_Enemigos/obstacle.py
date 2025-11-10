import pygame

class Obstacle:
    def __init__(self, x, y, width=50, height=50):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, camera_x):
        pygame.draw.rect(screen, (255, 0, 255),
                         pygame.Rect(self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
