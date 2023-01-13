import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class that represents a single alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading the alien image and assigning the rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the upper left corner of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Preservation of the exact horizontal position of the alien.
        self.x = float(self.rect.x)

    def update(self):
        """Moves the alien to the right."""
        self.rect.x += self.settings.alien_speed * self.settings.fleet_direction
        # self.rect.x = self.x # this is wrong, this is a mistake in the book

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:  # insteaf 0 screen_rect.left
            return True
