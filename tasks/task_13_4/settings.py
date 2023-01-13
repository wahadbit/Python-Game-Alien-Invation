class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Screen params
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (135, 246, 255)

        # Raindrop params
        self.raindrop_speed = 1
        self.raindrops_drop_speed = 10
        self.raindrops_direction = 1  # 1 - right; -1 - left.
