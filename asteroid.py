import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)

   def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, self.radius, 2) 

   def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
         return
      else:
         spawn_angle = random.uniform(20, 50)
         spawn_velo1 = self.velocity.rotate(spawn_angle)
         spawn_velo2 = self.velocity.rotate(-spawn_angle)
         spawn_radius = self.radius - ASTEROID_MIN_RADIUS
         little_one = Asteroid(self.position[0], self.position[1], spawn_radius)
         little_one.velocity = spawn_velo1 * 1.2
         little_two = Asteroid(self.position[0], self.position[1], spawn_radius)
         little_two.velocity = spawn_velo2 * 1.2





   def update(self, dt):
      self.position += (self.velocity * dt) 
      
