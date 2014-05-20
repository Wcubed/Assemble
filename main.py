__author__ = 'wybe'

import sys
import multiprocessing
import logging

import pygame
import pygame.locals as pyg_locals

import fileloader


COLORS = dict(black=(0, 0, 0), white=(255, 255, 255))


def main():

    logfile = "assemble.log"

    # --- Initialization ---

    # Initialize logfile and pygame.
    with open(logfile, 'w'):
        pass
    logging.basicConfig(filename=logfile,
                        format="%(asctime)s : %(levelname)s: %(message)s",
                        level=logging.DEBUG)
    pygame.init()

    logging.info("Pygame initialized.")

    # Set frame rate and create fps clock.
    fps = 60
    fps_clock = pygame.time.Clock()

    # Setup screen.
    screen = pygame.display.set_mode((1024, 640), pyg_locals.RESIZABLE)
    pygame.display.set_caption("Assemble")

    logging.info("Window created.")

    # --- Load items ---

    items = fileloader.load_objects()

    run = True

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

        location = [0, 0]

        for item in iter(items.values()):
            if item.sprite:
                screen.blit(item.sprite, location)
                location[0] += item.sprite.get_width()

        pygame.display.update()

        fps_clock.tick(fps)

    # --- Cleanup ---

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
