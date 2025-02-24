import pygame


class HealthBar:
    def __init__(self, entity, max_width=200, height=20, offset_y=20):
        self.entity = entity
        self.max_width = max_width
        self.height = height
        self.offset_y = offset_y
        self.gradient = {
            0.0: (255, 0, 0),    # Red
            0.5: (255, 255, 0),  # Yellow
            1.0: (0, 255, 0)     # Green
        }

    def update(self):
        self.current_ratio = self.entity.health / self.entity.max_health

    def draw(self, surface):
        # Position at entity's top
        bar_rect = pygame.Rect(
            self.entity.rect.centerx - self.max_width//2,
            self.entity.rect.top - self.offset_y,
            self.max_width,
            self.height
        )

        # Background bar
        pygame.draw.rect(surface, (40, 40, 40), bar_rect)

        # Current health with color interpolation
        current_color = self._get_gradient_color()
        current_width = int(self.max_width * self.current_ratio)
        health_rect = bar_rect.copy()
        health_rect.width = max(2, current_width)
        pygame.draw.rect(surface, current_color, health_rect)

    def _get_gradient_color(self):
        for threshold, color in sorted(self.gradient.items()):
            if self.current_ratio <= threshold:
                return color
        return self.gradient[1.0]
