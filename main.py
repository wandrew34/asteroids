# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from player import *
from constants import *

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    fpsclock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT /2

        player = Player(x,y)
        player.draw(screen)

        dt = fpsclock.tick(60) / 1000


if __name__ == "__main__":
    main()

