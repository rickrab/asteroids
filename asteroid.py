from circleshape import *
from constants import *
from logger import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50) # angle
            d1 = self.velocity.rotate(angle) # direction 1
            d2 = self.velocity.rotate(-angle) # direction 2
            self.radius -= ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, self.radius)
            a2 = Asteroid(self.position.x, self.position.y, self.radius)
            a1.velocity = d1 * 1.2
            a2.velocity = d2 * 1.2
