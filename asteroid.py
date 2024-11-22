import random
import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "brown", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def is_collided(self, other):
        total_radius = self.radius + other.radius
        if self.position.distance_to(other.position) <= total_radius:
            return True
        else:
            return False

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2