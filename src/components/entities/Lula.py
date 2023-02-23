import pygame as pg
from src.components.Config import GameConfig

game_config = GameConfig()


class Player(pg.sprite.Sprite):
    speed = 9
    score = 0
    can_shoot = False

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("src/sprites/lula.png")
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 240
        self.player_pos_x = self.rect.x
        self.player_pos_y = self.rect.y

    def update(self, pos):
        if self.rect.x > game_config.get_window_width():
            self.rect.x = 0
            self.player_pos_x = self.rect.x

        if self.rect.x < 0:
            self.rect.x = game_config.get_window_width()
            self.player_pos_x = self.rect.x

        if self.rect.y > game_config.get_window_height():
            self.rect.y = 0
            self.player_pos_y = self.rect.y

        if self.rect.y < 0:
            self.rect.y = game_config.get_window_height()
            self.player_pos_y = self.rect.y

        if pos == "right":
            self.rect.x = self.rect.x + (1 * self.speed)
            self.player_pos_x = self.rect.x

        if pos == "left":
            self.rect.x = self.rect.x - (1 * self.speed)
            self.player_pos_x = self.rect.x

        if pos == "up":
            self.rect.y = self.rect.y - (1 * self.speed)
            self.player_pos_y = self.rect.y

        if pos == "down":
            self.rect.y = self.rect.y + (1 * self.speed)
            self.player_pos_y = self.rect.y

    def move(self, group=None):
        keys = pg.key.get_pressed()

        if self.can_shoot and group is not None:
            self.shoot(group)

        if keys[pg.K_d]:
            self.update("right")

        if keys[pg.K_a]:
            self.update("left")

        if keys[pg.K_w]:
            self.update("up")

        if keys[pg.K_s]:
            self.update("down")

    def get_score(self):
        return self.score

    def shoot(self, group):
        start_ticks = pg.time.get_ticks()
        seconds = (pg.time.get_ticks() - start_ticks) / 1000
        # print(seconds)
        # Make the player shoot


