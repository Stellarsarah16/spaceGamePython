import pygame, math
from EnemyShip import EnemyShip
import random

class Mob:
    def __init__(self, player_x, player_y, count, radius) -> None:
        self.player_x = player_x
        self.player_y = player_y
        self.enemyCount = count
        self.radius = radius
        self.enemies = []

        self.spawn_enemies_around_player()

    def spawn_enemies_around_player(self):
        angle_offset = random.uniform(0, 2 * math.pi)
        angle_increment = 2 * math.pi / self.enemyCount

        for i in range(self.enemyCount):
            angle = angle_offset + i * angle_increment
            enemy_x = self.player_x + self.radius * math.cos(angle)
            enemy_y = self.player_y + self.radius * math.sin(angle)
            enemy = EnemyShip(enemy_x, enemy_y)
            self.enemies.append(enemy)

    def update(self, x, y):
        # For simplicity, let's move enemies towards the player
        for enemy in self.enemies:
            enemy.update((x, y))
            # Optionally, add attack logic or other behavior
            if enemy.can_attack():
                enemy.attack(self.player_x, self.player_y)
    
    def update_enemy_bullets(self, screen_width, screen_height):
        # Update bullets for all enemies
        for enemy in self.enemies:
            enemy.update_bullets(screen_width, screen_height)

    def draw_enemy_bullets(self):
        for idx, enemy in enumerate(self.enemies):
            #print(f"Enemy {idx+1} Bullets:")
            for bullet in enemy.bullets:
                print(f" - Position ({bullet.x}, {bullet.y})")

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        self.draw_enemy_bullets()
    

        
