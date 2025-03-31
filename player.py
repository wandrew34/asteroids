import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (0,255,0), self.triangle(), 2)
        

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        keys = pygame.key.get_pressed()
        print(type(keys))
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate( -dt )
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate( dt )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt    