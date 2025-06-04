# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    i = 1 #i is just for frame counting

    pygame.init()
    gp_updatable = pygame.sprite.Group()
    gp_drawable = pygame.sprite.Group()
    gp_asteroids = pygame.sprite.Group()
    gp_shots = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    AsteroidField.containers = gp_updatable
    Asteroid.containers = (gp_asteroids, gp_updatable, gp_drawable)    
    Player.containers = (gp_updatable, gp_drawable) 
    Shot.containers = (gp_shots, gp_updatable, gp_drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #group_checks
        #update instances
        for instance in gp_updatable:
            instance.update(dt)
        #check collision with asteroids
        for instance in gp_asteroids:
            if instance.is_collision(player):
                print("Game over!")
                exit()
        #draw everything
        for instance in gp_drawable:
            instance.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        # print framecount every 60 frames
        if i % 60 == 0:
            print(f"frame {i}")
        i += 1

        
if __name__ == "__main__":
    main()

