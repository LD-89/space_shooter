import pygame

from projectile import Projectile
from space_shooter_sprite import SpaceShooterSprite


class Player(SpaceShooterSprite):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.health = 100
        self.max_health = 100
        self.image = pygame.Surface((50, 60))
        self.image.fill((0, 128, 255))  # Blue
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)
        self.speed = 8
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = 0.5
        self.friction = -0.12
        self.shoot_cooldown = 300  # Milliseconds
        self.last_shot = 0
        self.projectiles = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        self.velocity.x = 0

        # Horizontal movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity.x += self.speed

        self.velocity.x += self.velocity.x * self.friction
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Vertical movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # Boundaries check
        self.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))

    def shoot(self, target_pos):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_cooldown:
            new_projectile = Projectile(
                self.screen_width,
                self.screen_height,
                self.rect.center,
                target_pos
            )
            self.projectiles.add(new_projectile)
            self.last_shot = current_time
            return new_projectile
