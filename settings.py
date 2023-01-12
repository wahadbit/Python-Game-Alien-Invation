class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (20, 20, 20)  # (230, 230, 230)
        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_color = (255, 128, 0)
        self.bullets_allowed = 3
