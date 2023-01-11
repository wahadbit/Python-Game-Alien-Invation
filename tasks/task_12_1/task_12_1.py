import sys

import pygame


class PygameBlueWindow():
    '''12.1. Синее небо: создайте окно Pygame с синим фоном.'''

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.bg_color = (135, 206, 235)

    def start(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == '__main__':
    ai = PygameBlueWindow()
    ai.start()
