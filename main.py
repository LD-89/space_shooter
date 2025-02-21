import pygame

from collisions_engine import check_collisions
from enemy import Enemy
from player import Player
from spawn_controller import SpawnController

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

#Initialize enemies
enemies = pygame.sprite.Group()
spawn_controller = SpawnController()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            projectile = player.shoot(pygame.mouse.get_pos())
            all_sprites.add(projectile)

    if spawn_controller.should_spawn():
        new_enemy = Enemy(SCREEN_WIDTH)
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

    enemies.update()
    all_sprites.update()

    check_collisions()

    screen.fill((0, 0, 0))  # Black background
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(120)  # FPS

pygame.quit()
