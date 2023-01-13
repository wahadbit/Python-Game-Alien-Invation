import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class that represents a single alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Loading the alien image and assigning the rect attribute.
        self.image = pygame.image.load('tasks\\task_13_2\\images\\star.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Preservation of the exact horizontal position of the alien.
        self.x = float(self.rect.x)
