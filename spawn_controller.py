import random

import pygame


class SpawnController:
    def __init__(self):
        self.last_spawn = pygame.time.get_ticks()
        self.spawn_interval = 2000  # 2 seconds
        self.variance = 500  # 500ms randomization

    def should_enemy_spawn(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn > self.spawn_interval:
            self.last_spawn = current_time
            self.spawn_interval = 2000 + random.randint(-self.variance, self.variance)
            return True
        return False
