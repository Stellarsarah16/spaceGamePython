import pygame, math
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        
        self.original_image = pygame.transform.scale(
            pygame.image.load('assets\Player\Pod\Pod1.png').convert_alpha(), (width, height))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        # position and velocity
        self.x = x
        self.y = y
        self.velocity = 0.0
        self.angle = 0.0
        self.angular_velocity = 0.0
        self.acceleration = 0.5

    def update(self):
        self.angle += self.angular_velocity

        # rotate
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center) 
        

        # Update position based on velocity and angle
        self.x += self.velocity * -math.sin(math.radians(self.angle))
        self.y += self.velocity * -math.cos(math.radians(self.angle))
        self.rect.center = (self.x, self.y)

    def rotate_left(self):
        self.angular_velocity = 1  # Adjust as needed

    def rotate_right(self):
        self.angular_velocity = -1  # Adjust as needed

    def stop_rotation(self):
        self.angular_velocity = 0.0

    def thrust(self):
        self.velocity += self.acceleration

    def stop_thrust(self):
        self.velocity = 0.0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color)

    def getStats(self):
        stats = (f"angle: {self.angle}, center: {self.rect.center}, rect: {self.rect}")
        return stats
    
    def scale_image(self, scale_factor):
        new_width = int(self.image.get_width() * scale_factor)
        new_height = int(self.image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))