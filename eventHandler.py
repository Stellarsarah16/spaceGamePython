import pygame
from player import Player

class EventHandler:
    def  __init__(self, player, main):
        self.player = player

        self.keydown_actions = {
            pygame.K_ESCAPE: main.setRunOff,
            (pygame.K_a, pygame.K_d): lambda: None,  # Do nothing for simultaneous A and D
            pygame.K_a: player.rotate_left,
            pygame.K_d: player.rotate_right,
            pygame.K_w: player.thrust,
            pygame.K_SPACE: lambda: player.shoot(player.angle)
        }

        self.keyup_actions = {
            pygame.K_a: player.stop_rotation,
            pygame.K_d: player.stop_rotation,  # Stop rotation for both A and D
            pygame.K_w: player.stop_thrust
        }
        self.events = pygame.event.get()

    # Process events
    def handleEvents(self, player, main):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key in self.keydown_actions:
                    self.keydown_actions[event.key]()
            
            elif event.type == pygame.KEYUP:
                if event.key in self.keyup_actions:
                    self.keyup_actions[event.key]()
    
 