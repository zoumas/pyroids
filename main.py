import pygame
import constants
from player import Player


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        # limits FPS to 60
        dt = clock.tick(60) / 1_000

    pygame.quit()


if __name__ == "__main__":
    main()
