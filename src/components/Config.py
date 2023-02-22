class GameConfig:
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 480
    level = 1

    def get_window_height(self):
        return self.SCREEN_HEIGHT

    def get_window_width(self):
        return self.SCREEN_WIDTH

    def get_window_width_height(self):
        return [self.SCREEN_WIDTH, self.SCREEN_HEIGHT]

    def get_level(self):
        return self.level

    def set_level(self, new_level):
        self.level = new_level

    def get_name_level(self):
        level = self.level
        if self.level == 1:
            return "Praça dos três poderes"
        elif self.level == 2:
            return "Orla de Icoaraci"
