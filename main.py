import pygame

from player import Player

# Initialize Pygame
pygame.init()

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Main game loop
running = True
clock = pygame.time.Clock()

# Initialize player and sprite group
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))  # Black background
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)  # FPS

pygame.quit()
