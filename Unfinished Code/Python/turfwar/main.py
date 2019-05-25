# Michael Freeman
# Turf War!

import pygame as py
from sprites import *
from settings import *

# Set up the screen.

# Initializes the game.
pg.init()

# Initializes sound.
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game.")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
# Game loop
running = True
while running:
    # Keep loop running at the right speed.
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # Check for closing the window.
        if event.type == pg.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / Render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display.
    pg.display.flip()

pg.quit()
