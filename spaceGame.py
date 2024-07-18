import pygame
from player import Player
from settings import *
from Mob import Mob

# Initialize the game
pygame.init()   
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Game')

background = pygame.transform.scale(pygame.image.load('assets\\Background\\spr_stars01.png').convert(), (WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()

# Create instance of Player
player = Player(400, 250, *PLAYER_SIZE)
#enemy = EnemyShip(400, 100)
all_sprites.add(player)
mob = Mob(player.x, player.y, 5, 200)

#enemies = []
#for x in range(ENEMY_COUNT):
#    enemies.append(EnemyShip(300 + (20*x), 100+(20*x)))

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # rotate and thrust
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_a & event.key == pygame.K_d):
                pass
            elif event.key == pygame.K_a:
                player.rotate_left()
            elif event.key == pygame.K_d:
                player.rotate_right()
            elif event.key == pygame.K_SPACE:
                player.thrust()
                
                print(player.getStats()) #print player stats for debug mode

        # stop rotation or thrust        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.stop_rotation()
            elif event.key == pygame.K_SPACE:
                player.stop_thrust()
                print(player.getStats()) #print player stats for debug mode


    all_sprites.update()
    #for enemy in enemies:
    #enemy.update((player.x, player.y))
    mob.update(player.x, player.y)
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw to screen
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    
    
    #for enemy in enemies:
    mob.draw(screen) 

    # Update the display
    pygame.display.flip()
    clock.tick(60)
