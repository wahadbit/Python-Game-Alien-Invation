import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """"""

    def __init__(self, ai_game):
        """"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создание снаряда в позиции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_height, self.settings.bullet_width)
        self.rect.center = ai_game.ship.rect.center

        # Позиция снаряда хранится в вещественном формате.
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает снаряд вверх по экрану."""

        # Обновление позиции снаряда в вещественном формате.
        self.x += self.settings.bullet_speed

        # Обновление позиции прямоугольника.
        self.rect.x = self.x

    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
