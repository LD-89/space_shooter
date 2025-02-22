import pygame

from enemy import Enemy
from player import Player
from projectile import Projectile


class GameState:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize all sprite entities group
        self.all_entities = pygame.sprite.Group()

        # Initialize player
        self.player = Player(screen_width, screen_height)
        self.all_entities.add(self.player)

        # Initialize sprite groups
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()

    def add_projectile(self, projectile: Projectile):
        self.projectiles.add(projectile)
        self.all_entities.add(projectile)

    def add_enemy(self):
        new_enemy = Enemy(self.screen_width, self.screen_height)
        self.enemies.add(new_enemy)
        self.all_entities.add(new_enemy)

    def update(self):
        self.all_entities.update()