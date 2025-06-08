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

    pygame.init()
    gp_updatable = pygame.sprite.Group()
    gp_drawable = pygame.sprite.Group()
    gp_asteroids = pygame.sprite.Group()
    gp_shots = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    asteroids_shot = 0
    time_alive = 0
    points_total = 0


    AsteroidField.containers = gp_updatable
    Asteroid.containers = (gp_asteroids, gp_updatable, gp_drawable)    
    Player.containers = (gp_updatable, gp_drawable) 
    Shot.containers = (gp_shots, gp_updatable, gp_drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    def game_stats():
        print(f"asteroids shot: {asteroids_shot}, time alive: {int(time_alive)}, shots fired: {player.shot_count}")
        points_total = int(((asteroids_shot * 10) + (time_alive / 2) - (player.shot_count / 6)) * 10)
        if points_total < 0:
            points_total = 0
        print(f"=== total points: {points_total} ===")

   
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
        for i_asteroid in gp_asteroids:
            if i_asteroid.is_collision(player):
                print("Game over!")
                game_stats()
                exit()
            for i_shot in gp_shots:
                if i_asteroid.is_collision(i_shot):
                    i_asteroid.split()
                    asteroids_shot += 1
                    i_shot.kill()
        #draw everything
        for instance in gp_drawable:
            instance.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        time_alive += 1 / 60
if __name__ == "__main__":
    main()

