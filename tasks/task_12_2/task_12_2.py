import sys

import pygame


class PygameBlueWindow():
    '''12.1. Синее небо: создайте окно Pygame с синим фоном.'''

    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.bg_color = (135, 206, 235)

        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load(
            '.\\tasks\\task_12_2\\images\\task_12_2_sonic.bmp')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        pygame.display.set_caption('Task 12.2')

    def start(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def bletme(self):
        self.screen.blit(self.image, self.rect)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill(self.bg_color)
        self.bletme()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    ai = PygameBlueWindow()
    ai.start()
