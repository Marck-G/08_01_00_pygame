import pygame
from settings import *
from particle import Particle

class Player:
    def __init__(self, x, y):
        """Initialize the player object."""
        self.rect = pygame.Rect(x, y, 72, 94) # Tamaño del sprite
        self.vel_y = 0
        self.speed = 5
        self.on_ground = False  # Indica si está sobre algún sólido
        # frames para caminar
        self.walk_frames = [
            pygame.image.load("assets/p1_walk01.png"),
            pygame.image.load("assets/p1_walk02.png"),
            pygame.image.load("assets/p1_walk03.png"),
            pygame.image.load("assets/p1_walk04.png"),
            pygame.image.load("assets/p1_walk05.png"),
            pygame.image.load("assets/p1_walk06.png"),
            pygame.image.load("assets/p1_walk07.png"),
            pygame.image.load("assets/p1_walk08.png"),
            pygame.image.load("assets/p1_walk09.png"),
            pygame.image.load("assets/p1_walk10.png"),
            pygame.image.load("assets/p1_walk11.png"),
        ]
        # frame para saltar
        self.jump_frame = pygame.image.load("assets/p1_jump.png")
        self.frame_index = 0
        self.animation_timer = 0
        self.moving = False
        # sonidos
        self.jump_sound = pygame.mixer.Sound("assets/jump_05.wav")
        self.jump_sound.set_volume(0.15)

    def handle_input(self):
        """Handle player input for movement and jumping."""
        keys = pygame.key.get_pressed()
        self.moving = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.moving = True
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and self.on_ground:
            self.vel_y = JUMP_STRENGTH
            self.on_ground = False
            self.jump_sound.play()
            # Partículas de polvo al despegar
            if hasattr(self, 'particles'):
                for _ in range(5):
                    self.particles.append(Particle(self.rect.centerx, self.rect.bottom, (200, 200, 200)))
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
         # Animación
        if not self.on_ground:
            image = self.jump_frame
        elif self.moving:
            self.animation_timer += 1
            if self.animation_timer >= 10:  # cambiar frame cada 10 ticks
                self.animation_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
            image = self.walk_frames[self.frame_index]
        else:
            image = self.walk_frames[0]

        screen.blit(image, (self.rect.x - camera_x, self.rect.y))
