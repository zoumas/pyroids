import pygame
import constants
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                return

        screen.fill("black")

        player.draw(screen)

        # refresh the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
