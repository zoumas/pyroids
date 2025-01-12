import pygame

import constants
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    AsteroidField()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for i in updatable:
            i.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                print("Game over!")
                running = False
                break
            for s in shots:
                if a.collides_with(s):
                    s.kill()
                    a.split()
                    break

        if not running:
            break

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        # limits FPS to 60
        dt = clock.tick(60) / 1_000

    pygame.quit()


if __name__ == "__main__":
    main()
