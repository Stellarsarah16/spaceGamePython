import pygame, math
from settings import *
from bullet import Bullet
from debug import debug

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, screen):
        super().__init__()
        self.screen = screen
        self.original_image = pygame.transform.scale(
            pygame.image.load('assets/Player/Pod/Pod1.png').convert_alpha(), (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        # position and velocity
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.maxVelocity = 5
        self.angle = 0.0
        self.angular_velocity = 0.0
        self.maxAngularVelocity = 5
        self.acceleration = .1

        #weapon
        self.bullets = []
        self.attacking = False
        self.shootCooldown = 500
        self.attackTime = None

    def update(self):
        self.input()
        self.cooldown()
        self.angle += self.angular_velocity

        # rotate
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center) 
        

        # Update position based on velocity and angle
        self.x += self.velocity * -math.sin(math.radians(self.angle))
        self.y += self.velocity * -math.cos(math.radians(self.angle))
        self.rect.center = (self.x, self.y)

        for bullet in self.bullets:
            x, y = bullet.getPos()
            print(bullet.getPos())
            if bullet.is_offscreen(x, y):    
                self.bullets.pop(0)
                print('destroyed')
            bullet.move()

        for bullet in self.bullets:
            bullet.draw(self.screen)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.angular_velocity < self.maxAngularVelocity:
                self.angular_velocity += .2  # Adjust as needed
        else:
            if self.angular_velocity > 0:
                self.angular_velocity -= .1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.angular_velocity > -self.maxAngularVelocity:
                self.angular_velocity -= .2  # Adjust as needed
        else:
            if self.angular_velocity < 0:
                self.angular_velocity += .1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.velocity < self.maxVelocity:
                self.velocity += self.acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.velocity > 0:
                self.velocity -= self.acceleration
        if keys[pygame.K_SPACE]:
            self.shoot(self.angle)            

    def shoot(self, angle):
        if self.attacking:
            return
        self.attackTime = pygame.time.get_ticks()
        self.bullets.append(Bullet(self.x, self.y, angle, 20))
        self.attacking = True
        
        #print(self.bullets[0])

    def draw(self, screen):
        pygame.draw.rect(self.screen, self.color)


    def getStats(self):
        stats = (f"angle: {self.angle}, center: {self.rect.center}, rect: {self.rect}")
        return stats
    
    def scale_image(self, scale_factor):
        new_width = int(self.image.get_width() * scale_factor)
        new_height = int(self.image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        (self.attackTime)
        if self.attacking:
            if self.attackTime != None:
                    if current_time - self.attackTime >= self.shootCooldown:
                        self.attacking = False

        
