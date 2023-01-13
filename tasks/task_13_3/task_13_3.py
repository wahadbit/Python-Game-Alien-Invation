import sys

import pygame

from settings import Settings
from raindrop import Raindrop


class Raindrops():
    '''13.1. Звезды'''

    def __init__(self):
        self.settings = Settings()
        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.bg_color = self.settings.bg_color

        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()

    def start(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_raindrops()
            self._update_screen()

    def _create_raindrops(self):
        """Создание каплей."""
        # Создание капли
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        # Определяет количество каплей в ряду
        available_space_x = self.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Определяет количество рядов, помещающихся на экране.
        available_space_y = self.screen_height - \
            (2 * raindrop_height)
        number_rows = available_space_y // (2 * raindrop_height)

        # Создание сетки из каплей.
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Создание капли и размещение ее в ряду."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
        self.raindrops.add(raindrop)

    def _check_raindrops_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.raindrops.sprites():
            if alien.check_edges():
                self._remove_raindrops()
                break

    def _remove_raindrops(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.raindrops.update()
        # Удаление снарядов, вышедших за край экрана.
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= 0:
                self.raindrops.remove(raindrop)

    def _update_raindrops(self):
        """Updates the positions of all raindrops."""
        self._check_raindrops_edges()
        self.raindrops.update()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""

        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.bg_color)
        self.raindrops.draw(self.screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    ai = Raindrops()
    ai.start()
