import sys

import pygame

from star import Star


class Stars():
    '''13.1. Звезды'''

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.bg_color = (0, 0, 0)

        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def start(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание звезды
        star = Star(self)
        star_width, star_height = star.rect.size

        # Определяет количество звезд в ряду
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Определяет количество рядов, помещающихся на экране.
        available_space_y = self.screen_height - \
            (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        # Создание звездной сетки.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Создание звезды и размещение ее в ряду."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.rect.x = star_width + 2 * star_width * star_number
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""

        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    ai = Stars()
    ai.start()
