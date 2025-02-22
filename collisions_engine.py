import pygame

from game_state import GameState


class CollisionsEngine():
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def check_collisions(self):
        # Player-enemy collisions
        pygame.sprite.spritecollide(
            self.game_state.player, self.game_state.enemies, True,
            pygame.sprite.collide_mask
        )

        # Projectile-enemy collisions
        pygame.sprite.groupcollide(
            self.game_state.projectiles, self.game_state.enemies,
            True, True,
            pygame.sprite.collide_rect_ratio(0.7)
        )

        # Boundary checks
        for entity in self.game_state.all_entities:
            entity.rect.clamp_ip(screen_rect)
