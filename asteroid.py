import pygame
import constants
import random
from circleshape import CircleShape
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            constants.LINE_WIDTH,
        )

    def update(self, dt):
        # move in a straight line at constant speed
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)
        radius = self.radius - constants.ASTEROID_MIN_RADIUS

        velocity_scale_factor = 1.2

        a1 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = v1 * velocity_scale_factor
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a2.velocity = v2 * velocity_scale_factor
