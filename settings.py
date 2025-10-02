class Settings():
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует настроки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_hight = 800
        self.bg_color = (230, 230, 230)

        #Настройка корабля
        self.ship_speed = 1.5

        #Параматеры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 22, 22)
        self.bullets_allowed = 100

        # Настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction = 1 обозначает движение вправо; a - 1 - влево
        self.fleet_direction = 1
            



