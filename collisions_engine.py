import pygame


def check_collisions():
    # Player-enemy collisions
    pygame.sprite.spritecollide(
        player, enemies, True,
        pygame.sprite.collide_mask
    )

    # Projectile-enemy collisions
    pygame.sprite.groupcollide(
        projectiles, enemies,
        True, True,
        pygame.sprite.collide_rect_ratio(0.7)
    )

    # Boundary checks
    for entity in all_sprites:
        entity.rect.clamp_ip(screen_rect)
