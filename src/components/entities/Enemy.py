import pygame as pg
from src.components.Config import GameConfig
from random import randint

game_config = GameConfig()


class BolsonaroEnemy(pg.sprite.Sprite):
    clicked = False

    def __init__(self):
        super().__init__()
        self.image = pg.image.load("src/sprites/bozo.png")
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, game_config.get_window_width() - 125)
        self.rect.y = randint(0, game_config.get_window_height() - 125)
        self.player_pos_x = self.rect.x
        self.player_pos_y = self.rect.y

    def update(self, sprite_group, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                for sprite in sprite_group:
                    if sprite.rect.collidepoint(event.pos):
                        self.clicked = True

