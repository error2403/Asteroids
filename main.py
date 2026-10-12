import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    # print initial game settings/info
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    # start game loop
    while True:
        # log game info
        log_state()

        # check for player input
        for event in pygame.event.get():

            # exit game if player quits
            if event.type == pygame.QUIT:
                return


        screen.fill("black")
        # draw new screen
        pygame.display.flip()

        # update pygame delta clock
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
