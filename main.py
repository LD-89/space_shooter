import pygame

from collisions_engine import CollisionsEngine
from game_state import GameState
from interface.health_bar import HealthBar
from interface.score_display import ScoreDisplay
from interface.user_interface import UserInterface
from spawn_controller import SpawnController

# Initialize Pygame
pygame.init()

# Window settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

game_state = GameState(SCREEN_WIDTH, SCREEN_HEIGHT)
spawn_controller = SpawnController()
ui = UserInterface((SCREEN_WIDTH, SCREEN_HEIGHT))
health_bar = HealthBar(game_state.player)
score_display = ScoreDisplay()

ui.pause_menu.hide()

while game_state.running:
    time_delta = clock.tick(120) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_state.paused:
                    unpause_game()
                else:
                    pause_game()
        if event.type == pygame.QUIT:
            game_state.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            projectile = game_state.player.shoot(pygame.mouse.get_pos())
            game_state.add_projectile(projectile)

        result = ui.handle_events(event)
        if result == "resume":
            unpause_game()

    ui.manager.update(time_delta)

    if not game_state.paused:
        if spawn_controller.should_enemy_spawn():
            game_state.add_enemy()

        game_state.update()
        health_bar.update()
        game_state = CollisionsEngine(game_state).check_collisions()
        score_display.add(game_state.enemies_killed * 100)

    screen.fill((0, 0, 0))  # Black background
    game_state.all_entities.draw(screen)
    health_bar.draw(screen)
    score_display.draw(screen)
    ui.draw(screen)
    pygame.display.flip()
    clock.tick(120)  # FPS

pygame.quit()
