import pygame

from enemy import Enemy
from interface.user_interface import UserInterface
from player import Player
from projectile import Projectile


class GameState:
    def __init__(self, screen_width: int, screen_height: int):
        self.running = True
        self.paused = False


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

        self.enemies_killed = 0

    def add_projectile(self, projectile: Projectile):
        self.projectiles.add(projectile)
        self.all_entities.add(projectile)

    def add_enemy(self):
        new_enemy = Enemy(self.screen_width, self.screen_height)
        self.enemies.add(new_enemy)
        self.all_entities.add(new_enemy)

    def update(self):
        self.all_entities.update()

    def pause_game(self, ui: UserInterface):
        self.paused = True
        ui.pause_menu.show()

    def unpause_game(self, ui: UserInterface):
        self.paused = False
        ui.pause_menu.hide()