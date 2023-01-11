class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0) #(230, 230, 230)
        self.ship_speed = 1.5