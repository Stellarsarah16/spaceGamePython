import pygame, math
from enemy import enemy
from bullet import Bullet
import random

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.original_image = pygame.image.load('assets\Player\Pod\ship2.png').convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.health = 100
        self.bullets = []
        self.attack_cooldown = random.randint(100, 300)  # Random initial cooldown
        self.current_cooldown = 0  # Current cooldown timer

        # position and velocity
        self.x = x
        self.y = y
        self.velocity = 2.0
        self.angle = 0.0
        self.angular_velocity = 1.0
        self.acceleration = 1

    def update(self, player_pos):
        # Calculate angle towards player
        target_angle = -math.degrees(math.atan2(player_pos[1] - self.y, player_pos[0] - self.x))
        
        # Adjust angle gradually towards the target angle
        angle_diff = (target_angle - self.angle) % 360
        if angle_diff > 180:
            angle_diff -= 360
        elif angle_diff < -180:
            angle_diff += 360
        self.angular_velocity = angle_diff / 5.0  # Adjust the divisor for rotation speed

        # rotate
        self.angle += self.angular_velocity
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center) 
        
        # Update position based on velocity and angle
        self.x += self.velocity * -math.sin(math.radians(self.angle))
        self.y += self.velocity * -math.cos(math.radians(self.angle))
        self.rect.center = (self.x, self.y)

        #shoot on random interval


    def set_rotation_speed(self, speed):
        self.angular_velocity = speed

    def set_velocity(self, velocity):
        self.velocity = velocity

    def stop_movement(self):
        self.angular_velocity = 0.0
        self.velocity = 0.0

    def draw(self, screen):
        #pygame.draw.rect(screen, self.color)
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)

    def getStats(self):
        #stats = (f"angle: {self.angle}, center: {self.rect.center}, rect: {self.rect}")
        stats = {
            'angle': self.angle,
            'center': self.rect.center,
            'rect': self.rect
        }
        return stats
    
    def scale_image(self, scale_factor):
        new_width = int(self.image.get_width() * scale_factor)
        new_height = int(self.image.get_height() * scale_factor)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))

    def attack(self, target_x, target_y):
        bullet = Bullet(self.x, self.y, target_x, target_y, 20)
        self.bullets.append(bullet)

    def can_attack(self):
        # Check if enemy can attack based on cooldown
        if self.current_cooldown <= 0:
            self.current_cooldown = self.attack_cooldown
            return True
        else:
            self.current_cooldown -= 1
            return False

    def update_bullets(self, screen_width, screen_height):
        # Update bullets' positions
        for bullet in self.bullets:
            bullet.move()
        
        # Remove offscreen bullets
        self.bullets = [bullet for bullet in self.bullets if not bullet.is_offscreen(screen_width, screen_height)]
