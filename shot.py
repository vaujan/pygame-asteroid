import pygame
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def is_collided(self, other):
        total_radius = self.radius + other.radius
        if self.position.distance_to(other.position) <= total_radius:
            return True
        else:
            return False