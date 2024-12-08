from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)

    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable_group:
            obj.update(dt)

        screen.fill("black")
        for obj in drawable_group:
            obj.draw(screen)
        pygame.display.flip()

        delta = clock.tick(60)
        dt = delta/1000



        



if __name__ == "__main__":
    main()