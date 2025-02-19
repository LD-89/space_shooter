import random

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 60))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = 8
        self.spawn_time = pygame.time.get_ticks()  # Track creation time
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        self.rect.y += self.speed

        # Remove when exiting screen
        if self.rect.top > self.screen_height:
            self.kill()

        # Optional horizontal movement
        if random.random() < 0.02:  # 2% chance per frame
            self.rect.x += random.randint(-5, 5)
            self.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))
