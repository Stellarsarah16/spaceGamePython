import pygame, sys
from player import Player
from settings import *
from Mob import Mob
from EnemyShip import EnemyShip
from eventHandler import EventHandler

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Space Game')

        self.background = pygame.transform.scale(pygame.image.load('assets\\Background\\spr_stars01.png').convert(), (WIDTH, HEIGHT))

        self.all_sprites = pygame.sprite.Group()

        self.player = Player(400, 250, *PLAYER_SIZE, self.screen)
        self.all_sprites.add(self.player)

        self.enemy = EnemyShip(400, 100)
        # self.mob = Mob(self.player.x, self.player.y, 5, 200)
        #self.event_handler = EventHandler(self.player, self)

    def run(self):
        
        while True:
            #self.event_handler.handleEvents(self.player, self)

            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    self.quit()
                    sys.exit()
            self.all_sprites.update()
            self.enemy.update((self.player.x, self.player.y))
            # self.mob.update(self.player.x, self.player.y)

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.draw(self.screen)

            self.enemy.draw(self.screen)
            # self.mob.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

    def quit(self):
        pygame.quit()
        exit()

    def setRunOff(self):
        self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()
    game.quit()
