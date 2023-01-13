import sys
from random import randint
import pygame

from star import Star


class Stars():
    '''13-2. Better Stars'''

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.bg_color = (0, 0, 0)

        self.stars = pygame.sprite.Group()
        self._create_fleet()

    def start(self):
        """Starting the main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _create_fleet(self):
        """Creation of an invasion fleet."""
        # Making a star
        star = Star(self)
        star_width, star_height = star.rect.size

        # Specifies the number of stars in a row
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Specifies the number of rows to fit on the screens.
        available_space_y = self.screen_height - \
            (2 * star_height)
        number_rows = available_space_y // (2 * star_height)

        # Create a star grid.
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Creating a star and placing it in a row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        random_number = randint(-10, 10)
        star.rect.x = star_width + \
            ((2 * star_width) + random_number) * star_number
        star.rect.y = star.rect.height + \
            ((2 * star.rect.height) + random_number) * row_number

        self.stars.add(star)

    def _update_screen(self):
        """Refreshes the images on the screen and displays the new screen."""
        # The screen is redrawn on each iteration of the loop.
        self.screen.fill(self.bg_color)
        self.stars.draw(self.screen)
        # Display the last screen drawn.
        pygame.display.flip()


if __name__ == '__main__':
    ai = Stars()
    ai.start()
