import pygame as pg


class Bullet(pg.sprite.Sprite):
    def __init__(self, player_pos_x, player_pos_y):
        super().__init__()
        self.image = pg.image.load("src/sprites/bullet1.png")
        self.rect = self.image.get_rect()
        self.rect.x = player_pos_x + 4
        self.rect.y = (player_pos_y / 2)

