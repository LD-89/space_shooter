import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((50, 60))
        self.image.fill((0, 128, 255))  # Blue
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)
        self.speed = 8
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = 0.5
        self.friction = -0.12
        self.screen_width = screen_width
        self.screen_height = screen_height

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
