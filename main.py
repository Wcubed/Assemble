__author__ = 'wybe'

import sys

import pygame
import pygame.locals as pyg_locals

import objects


COLORS = dict(black=(0, 0, 0))


def main():

    # Initialize pygame
    pygame.init()

    # Set frame rate and create fps clock
    fps = 60
    fps_clock = pygame.time.Clock()

    # Setup screen
    screen = pygame.display.set_mode((500, 500), pyg_locals.RESIZABLE)
    pygame.display.set_caption("Assemble")

    run = True

    run = objects.load()

    # --- Main loop ---
    while run:

        # --- Event processing ---

        for event in pygame.event.get():
            if event.type == pyg_locals.QUIT:
                run = False
            elif event.type == pyg_locals.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict["size"], pyg_locals.RESIZABLE)

        # --- Game logic ---

        # --- Drawing ---
        screen.fill(COLORS['black'])

        pygame.display.update()

        fps_clock.tick(fps)

    # --- Cleanup ---

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()