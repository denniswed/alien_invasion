class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (195, 195, 195)

        #ship settings
        self.ship_limit = 3

        #bullet settings
        self.bullet_height = 15
        self.bullet_color = (20, 20, 20)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 15

        # Debug available, true or false
        self.alien_debug = True

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 0.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.25
        self.bullet_width = 5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        #ALien point value increase
        self.alien_points = int(self.alien_points * self.score_scale)
        