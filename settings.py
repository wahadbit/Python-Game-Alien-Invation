class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Screen params
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0)  # (230, 230, 230)

        # Ship params
        self.ship_speed = 1.2

        # Bullet params
        self.bullet_speed = 1.5
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = (255, 128, 0)
        self.bullets_allowed = 3

        # Alien params
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - right; -1 - left.
