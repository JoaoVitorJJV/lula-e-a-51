import pygame as pg
from src.components.GameEngine import Game

# Initialise pygame
pg.init()

# Title of window
pg.display.set_caption("Lula & 51")

# Engine
game = Game()
clock = pg.time.Clock()

# Main loop, run until window closed
running = True
while running:
    # Check events
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    game.init_game(events)
    pg.display.flip()
    clock.tick(60)

# close pygame
pg.quit()
