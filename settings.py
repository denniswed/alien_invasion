class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (195, 195, 195)

        #ship settings
        self.ship_speed = 0.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 900
        self.bullet_height = 15
        self.bullet_color = (20, 20, 20)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 0.25
        self.fleet_drop_speed = 15
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
