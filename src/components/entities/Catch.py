import pygame as pg
from random import randint
from src.components.entities.Lula import Player
from src.components.Config import GameConfig
from src.components.SoundTracker import Sound

game_config = GameConfig()


class Cachaca(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("src/sprites/cachaca.png")
        self.rect = self.image.get_rect()
        random_number_x = randint(0, game_config.get_window_width())
        random_number_y = randint(0, 380)

        self.rect.x = random_number_x
        self.rect.y = random_number_y

        # SoundTracker
        self.sound_tracker = Sound()

    def update(self):
        random_number_x = randint(0, game_config.get_window_width())
        random_number_y = randint(0, game_config.get_window_height())
        self.rect.x = random_number_x
        self.rect.y = random_number_y

    def check_colision(self, sprite_b):
        if self.rect.colliderect(sprite_b):
            Player.score = Player.score + 1
            self.sound_tracker.play_music_catch_cachaca("src/sounds/lula_score.mp3", 0.4)
            self.update()

