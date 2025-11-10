import pygame
from settings import *

class Player:
    def __init__(self, x, y):
        """Initialize the player object."""
        self.rect = pygame.Rect(x, y, 50, 50)
        self.vel_y = 0
        self.speed = 5
        self.on_ground = False  # Indica si está sobre algún sólido

    def handle_input(self):
        """Handle player input for movement and jumping."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False  # Saltó, ya no está en el suelo

    def apply_physics(self, platforms):
        """Apply physics to the player, including gravity and collisions."""
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Reiniciamos on_ground cada frame
        self.on_ground = False

        # Colisiones con plataformas (solo desde arriba)
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # Verificamos que el jugador cae sobre la plataforma
                if self.vel_y > 0 and self.rect.bottom <= platform.rect.bottom:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True

    def draw(self, screen, camera_x):
        """Draw the player on the screen, adjusted for camera position."""
        pygame.draw.rect(screen, COLOR_PLAYER,
                         pygame.Rect(self.rect.x - camera_x, self.rect.y, self.rect.width, self.rect.height))
