import sys

import pygame


class PygameBlueWindow():
    '''12.5. Клавиши'''

    def __init__(self):
        self.screen = pygame.display.set_mode((200, 200))
        self.bg_color = (0, 0, 0)

    def start(self):
        """Запуск основного цикла игры."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)

            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == '__main__':
    ai = PygameBlueWindow()
    ai.start()
