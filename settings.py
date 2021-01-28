class Settings:
    " " "A class to store all alien invasion settings" " "
    def __init__(self):
        # screen settings

        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed_factor = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60


