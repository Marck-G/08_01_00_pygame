import pygame
import sys


# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Set window size
pygame.display.set_caption("Simple Pygame Window") # Set window title

# Time controller for frame rate
clock = pygame.time.Clock()

# player variables
player_size = (50, 50)
player_x = WIDTH // 2 
player_y = HEIGHT - player_size[1] - 50 # start in the floor
player_color = (0, 128, 255)
player_seed = 5
player_velocity_y = 0

# Physics variables
gravity = 0.5
jump_strength = -10

# Floor
floor_rect = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)

# Main loop
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 2. Players Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_seed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_seed
    if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
        if player_y + player_size[1] >= floor_rect.top: # only jump if on the floor
            player_velocity_y = jump_strength
    
    # 3. Phisics Updates
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Collision with floor
    if player_y + player_size[1] >= floor_rect.top:
        player_y = floor_rect.top - player_size[1]
        player_velocity_y = 0

    # 3. Rendering
    screen.fill((30, 30, 30)) # Fill the screen with a color (dark gray)
    pygame.draw.rect(screen, player_color, (player_x, player_y, *player_size))
    pygame.draw.rect(screen, (100, 200, 100), floor_rect)
    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60) # Limit to 60 frames per second

# Clean up and exit
pygame.quit()
sys.exit()
