import pygame
import sys

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plataformas Básicas")

clock = pygame.time.Clock()

# Variables del jugador
player_color = (0, 128, 255)
player_speed = 5
player_rect = pygame.Rect(WIDTH // 2, HEIGHT - 100, 50, 50)
player_velocity_y = 0

# Física
gravity = 0.5
jump_strength = -10

# Plataformas
platforms = [
    pygame.Rect(0, HEIGHT - 50, WIDTH, 50),       # suelo
    pygame.Rect(150, 450, 200, 20),
    pygame.Rect(450, 350, 200, 20),
    pygame.Rect(300, 250, 150, 20)
]

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
        print(player_rect.bottom)
        for platform in platforms:
            isOnPlatform = isOnPlatform or(player_rect.bottom == platform.top)
            print("Player on platform: {}, \n\tPlatform Top: {}\n\tPlayer Bottom: {}".format(isOnPlatform, platform.top, player_rect.bottom))
        # only jump if on the floor
        if isOnPlatform:
            player_velocity_y = jump_strength

    # Física
    player_velocity_y += gravity
    player_rect.y += player_velocity_y

    # Colisiones con plataformas
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_rect.bottom = platform.top
            player_velocity_y = 0

    # Dibujar
    screen.fill((30, 30, 30))
    for platform in platforms:
        pygame.draw.rect(screen, (100, 200, 100), platform)
    pygame.draw.rect(screen, player_color, player_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
