from constants import PLAYER_SPEED, ASTEROID_MIN_RADIUS
import pygame
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position ,self.radius, 2)

    def update(self, dt):
        self.position +=  (self.velocity * dt)

    def split(self):
        self.kill() 
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            deviation = random.uniform(20, 50)
            new_v1 = pygame.Vector2(self.velocity).rotate(deviation)
            new_v2 = pygame.Vector2(self.velocity).rotate(-deviation)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_1.velocity = new_v1 * 1.2
            ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
            ast_2.velocity = new_v2 * 1.2


        

        

    
