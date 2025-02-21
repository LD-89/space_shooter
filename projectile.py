
import pygame
import math

from space_shooter_sprite import SpaceShooterSprite


class Projectile(SpaceShooterSprite):
    def __init__(self, screen_width, screen_height, start_pos, target_pos, speed=12):
        super().__init__(screen_width, screen_height)
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 255, 0))  # Yellow
        self.rect = self.image.get_rect(center=start_pos)

        # Calculate initial trajectory vector
        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]
        distance = max(1, math.hypot(dx, dy))

        self.velocity = pygame.math.Vector2(
            (dx / distance) * speed,
            (dy / distance) * speed
        )
        self.spawn_time = pygame.time.get_ticks()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        self.rect.centerx += self.velocity.x
        self.rect.centery += self.velocity.y

        # Auto-destruct after screen exit
        if not pygame.Rect(0, 0, self.screen_width, self.screen_height).colliderect(self.rect):
            self.kill()
