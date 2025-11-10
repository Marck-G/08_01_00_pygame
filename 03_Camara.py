import pygame
import sys

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scroll Horizontal")

clock = pygame.time.Clock()

# Variables del jugador
player_color = (0, 128, 255)
player_speed = 5
player_rect = pygame.Rect(100, HEIGHT - 100, 50, 50)
player_velocity_y = 0

# Física
gravity = 0.5
jump_strength = -15

# Mundo
LEVEL_WIDTH = 2000
platforms = [
    pygame.Rect(0, HEIGHT - 50, LEVEL_WIDTH, 50),
    pygame.Rect(200, 400, 80, 40),
    pygame.Rect(500, 250, 10, 40),
    pygame.Rect(800, 300, 40, 30),
    pygame.Rect(1000, 200, 150, 10)
]

camera_x = 0

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_rect.x += player_speed
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and player_velocity_y == 0:
        isOnPlatform = False
        for platform in platforms:
            isOnPlatform = isOnPlatform or(player_rect.bottom == platform.top)
            print("Player on platform: {}, \n\tPlatform Top: {}\n\tPlayer Bottom: {}".format(isOnPlatform, platform.top, player_rect.bottom))
        # only jump if on the floor
        if isOnPlatform:
            player_velocity_y = jump_strength

    # Física
    player_velocity_y += gravity
    player_rect.y += player_velocity_y

    # Colisiones
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_rect.bottom = platform.top
            player_velocity_y = 0

    # Actualizar cámara
    camera_x = player_rect.centerx - WIDTH // 2
    camera_x = max(0, min(camera_x, LEVEL_WIDTH - WIDTH))

    # Dibujar
    screen.fill((30, 30, 30))
    for platform in platforms:
        pygame.draw.rect(screen, (100, 200, 100),
                         pygame.Rect(platform.x - camera_x, platform.y, platform.width, platform.height))
    pygame.draw.rect(screen, player_color,
                     pygame.Rect(player_rect.x - camera_x, player_rect.y, player_rect.width, player_rect.height))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
