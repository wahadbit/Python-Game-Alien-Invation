import pygame


class Ship():

    def __init__(self, ai_game):
        ''''''

        self.aigame = ai_game
        self.screen = self.aigame.screen
        self.image = pygame.image.load(
            '.\\tasks\\task_12_6\\images\\fighter.bmp')

        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.aigame.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.aigame.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.aigame.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.aigame.settings.ship_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def bletme(self):
        self.screen.blit(self.image, self.rect)
