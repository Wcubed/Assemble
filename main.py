__author__ = 'wybe'

import pygame
import sys
from pygame.locals import *


pygame.init()


FPS = 60
FPS_CLOCK = pygame.time.Clock()


def main():

    screen = pygame.display.set_mode((500, 500), RESIZABLE)
    pygame.display.set_caption("Assemble")

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict["size"], RESIZABLE)

        screen.fill((0, 0, 0))

        pygame.display.update()

        FPS_CLOCK.tick(FPS)

    return

if __name__ == "__main__":
    main()