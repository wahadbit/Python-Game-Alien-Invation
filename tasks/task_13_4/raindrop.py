import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """Класс, представляющий одного пришельца."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load(
            'tasks\\task_13_4\\images\\raindrop.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца.
        self.y = float(self.rect.y)

    def update(self):
        """Moves the alien to the bottom."""
        self.rect.y += self.settings.raindrop_speed * self.settings.raindrops_direction
        # self.rect.x = self.x # this is wrong, this is a mistake in the book

    def check_edges(self):
        """Возвращает True, если капля находится у нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
