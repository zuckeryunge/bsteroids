import pygame
from circleshape import *
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.wait_shoot = 0
        self.shot_count = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        go = pygame.Vector2(0 ,1).rotate(self.rotation)
        go = go * (PLAYER_SPEED * dt)
        self.position = self.position + go

    def shoot(self):
        pew = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        pew.velocity = pygame.Vector2(0, 1)
        pew.velocity.rotate_ip(self.rotation)
        pew.velocity *= PLAYER_SHOOT_SPEED
        self.wait_shoot = PLAYER_SHOOT_COOLDOWN
        self.shot_count += 1;
        


    def update(self, dt):
        if self.wait_shoot > 0:
            self.wait_shoot -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt) 
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt) 
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            if self.wait_shoot <= 0:
                self.shoot()
                
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0;
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0;
