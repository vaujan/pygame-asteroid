"""
Asteroid Class Module

This module is part of a learning project implementing the classic Asteroids game.
It demonstrates object-oriented programming concepts and game physics.

Learning concepts demonstrated:
- Class inheritance (inherits from CircleShape)
- Vector mathematics (rotation and movement)
- Game object lifecycle management
"""

import random
import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    """
    Represents an asteroid in the game.
    
    This class demonstrates several key programming concepts:
    - Object initialization with inheritance
    - Vector-based movement
    - Collision detection
    - Object splitting mechanics
    
    The asteroid can move, detect collisions, and split into smaller asteroids
    when hit, showcasing game physics and object management.
    """
    
    def __init__(self, x, y, radius):
        """
        Initialize an asteroid.
        
        Args:
            x (float): Initial x position
            y (float): Initial y position
            radius (float): Asteroid's radius
        """
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        """
        Draw the asteroid on the screen.
        
        Args:
            screen: Pygame screen surface to draw on
        """
        pygame.draw.circle(screen, "brown", self.position, self.radius)

    def update(self, dt):
        """
        Update asteroid position based on velocity and time.
        
        Args:
            dt (float): Time delta for frame-rate independent movement
        """
        self.position += self.velocity * dt
        
    def is_collided(self, other):
        """
        Check if this asteroid collides with another object.
        
        Learning note: This implements basic circle collision detection
        using distance calculation between centers.
        
        Args:
            other: Another game object to check collision with
        Returns:
            bool: True if collision detected, False otherwise
        """
        total_radius = self.radius + other.radius
        if self.position.distance_to(other.position) <= total_radius:
            return True
        else:
            return False

    def split(self):
        """
        Split the asteroid into two smaller ones.
        
        Learning concepts demonstrated:
        - Vector rotation for direction
        - Object creation and destruction
        - Size management with constants
        - Velocity manipulation
        
        This method showcases how game objects can be dynamically created
        and modified based on game events.
        """
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating current velocity
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2
        
        # Spawn two new smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2