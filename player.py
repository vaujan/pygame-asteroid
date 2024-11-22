import pygame
from constants import *
from circleshape import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0.5
        self.button_spam_cooldown = 0.02

    def triangle(self):
        # Calculate triangle points for player ship
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Point upward by default
        right = forward.rotate(90)
        
        # Calculate three points of triangle
        nose = self.position + forward * self.radius
        left_wing = self.position - forward * (self.radius/2) - right * (self.radius/2)
        right_wing = self.position - forward * (self.radius/2) + right * (self.radius/2)
        
        return [nose, left_wing, right_wing]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)       
        if keys[pygame.K_d]:
            self.rotate(dt)       
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.move(dt * 2)

        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        # Then handle shooting
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                new_shot = self.shoot()
                if new_shot:
                    self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
                return new_shot

    def is_collided(self, other):
        total_radius = self.radius + other.radius
        if self.position.distance_to(other.position) <= total_radius:
            return True
        else:
            return False
    
    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return shot
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "lightblue", self.triangle(), 2)