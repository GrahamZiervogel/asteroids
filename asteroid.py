import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            up_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            up_velocity = self.velocity.rotate(random_angle)
            up_asteroid.velocity = up_velocity * 1.2

            down_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            down_velocity = self.velocity.rotate(-random_angle)
            down_asteroid.velocity = down_velocity * 1.2
