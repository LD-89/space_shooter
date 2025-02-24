import pygame


class ScoreDisplay:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
        self._cache = {}

    def add(self, points):
        self.value += points

    def draw(self, surface):
        if self.value not in self._cache:
            text_surface = self.font.render(
                f"Score: {self.value}",
                True, (255, 255, 255)
            )
            self._cache[self.value] = text_surface
        surface.blit(self._cache[self.value], (10, 10))
