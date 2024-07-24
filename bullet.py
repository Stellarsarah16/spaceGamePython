import pygame, math
from settings import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed = 1, target_x=None, target_y=None):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.transform.scale(
            pygame.image.load('assets/Other/beam1.png').convert_alpha(), (10, 20))
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.speed = speed
        self.width, self.height = pygame.display.get_surface().get_size()
        self.angle = angle
        
    def getPos(self):
        return self.x, self.y

    def is_offscreen(self, screen_width, screen_height):
        # Check if bullet is offscreen
        if (self.x < 0 or self.x > screen_width or
            self.y < 0 or self.y > screen_height):
            return True
        return False
    
    def move(self):
        self.x += self.speed * -math.sin(math.radians(self.angle))
        self.y += self.speed * -math.cos(math.radians(self.angle))
        self.rect.center = (self.x, self.y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
