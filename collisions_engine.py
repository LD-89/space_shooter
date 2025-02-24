import pygame

from game_state import GameState


class CollisionsEngine():
    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.screen_rect = pygame.Rect(0, 0, self.game_state.screen_width, self.game_state.screen_height)

    def check_collisions(self) -> GameState:
        # Player-enemy collisions
        pygame.sprite.spritecollide(
            self.game_state.player, self.game_state.enemies, True,
            pygame.sprite.collide_mask
        )

        # Projectile-enemy collisions
        collisions = pygame.sprite.groupcollide(
            self.game_state.projectiles, self.game_state.enemies,
            True, True,
            pygame.sprite.collide_rect_ratio(0.7)
        )
        self.game_state.enemies_killed += len(collisions)

        # Boundary checks
        for entity in self.game_state.all_entities:
            entity.rect.clamp_ip(self.screen_rect)

        return self.game_state
