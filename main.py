import pygame

from collisions_engine import CollisionsEngine
from game_state import GameState
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

game_state = GameState(SCREEN_WIDTH, SCREEN_HEIGHT)
spawn_controller = SpawnController()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            projectile = game_state.player.shoot(pygame.mouse.get_pos())
            game_state.add_projectile(projectile)

    if spawn_controller.should_enemy_spawn():
        game_state.add_enemy()

    game_state.update()
    CollisionsEngine(game_state).check_collisions()

    screen.fill((0, 0, 0))  # Black background
    game_state.all_entities.draw(screen)
    pygame.display.flip()
    clock.tick(120)  # FPS

pygame.quit()
