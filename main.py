import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screen_size)

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatables, drawables)

    Player.containers = (updatables, drawables)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatables, drawables)

    # game loop:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT")
                return

        screen.fill("black")

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                exit(0)

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

        for drawable in drawables:
            drawable.draw(screen)

        # refresh the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1_000


if __name__ == "__main__":
    main()
