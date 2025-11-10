import pygame
import sys


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600)) # Set window size
pygame.display.set_caption("Simple Pygame Window") # Set window title

# Time controller for frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 2. Game Logic Updates

    # 3. Rendering
    screen.fill((30, 30, 30)) # Fill the screen with a color (dark gray)

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60) # Limit to 60 frames per second

# Clean up and exit
pygame.quit()
sys.exit()
