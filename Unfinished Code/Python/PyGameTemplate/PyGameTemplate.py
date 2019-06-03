# PyGame template
import pygame
import random


# Set up the screen.
WIDTH = 360
HEIGHT = 480
FPS = 30

# Set up colors.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 225)

# Initializes the game.
pygame.init()

# Initializes sound.
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game.")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
    # Keep loop running at the right speed.
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing the window.
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display.
    pygame.display.flip()

pygame.quit()
