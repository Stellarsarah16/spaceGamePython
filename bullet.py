import pygame, math
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y, speed=5):
        width, height = 10, 20  
        self.original_image = pygame.transform.scale(
            pygame.image.load('assets\\Other\\beam1.png').convert_alpha(), (5, 10))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.distance_to_travel = math.sqrt((target_x - x)**2 + (target_y - y)**2)
        self.dx = (target_x - x) / self.distance_to_travel
        self.dy = (target_y - y) / self.distance_to_travel
        self.speed = speed

        self.move()

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def is_offscreen(self, screen_width, screen_height):
        # Check if bullet is offscreen
        if (self.x < 0 or self.x > screen_width or
            self.y < 0 or self.y > screen_height):
            return True
        return False
    
    def draw(self, screen):
        #pygame.draw.rect(screen, self.color)
        screen.blit(self.image, self.rect)
