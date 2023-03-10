import pygame as pg
from src.components.entities.Lula import Player
from src.components.Config import GameConfig

game_config = GameConfig()


class TextInterface:

    def __init__(self):
        pg.font.init()
        self.player = Player()
        self.font = pg.font.SysFont("Comic Sans Ms", 27, True)

    def draw_level_text(self, screen, level, color):
        text = ""
        text2 = ""
        if level == 1:
            text = "Pegue a garrafa de 51!"
        elif level == 2:
            text = "Clique no bolsonabo para passar!"
        elif level == 3:
            text = "Pegue os caroços de açaí e derrote a polícia!"
            text2 = "Use o mouse para atirar"
        text_surface = self.font.render(text, True, color)
        screen.blit(text_surface, (4, 0))
        if level == 3:
            text_surface2 = self.font.render(text2, True, color)
            screen.blit(text_surface2, (4, 28))

    def draw_score(self, screen, level, color):
        score = f"Pontuação: {self.player.get_score()}"
        score_text = self.font.render(score, True, color)
        screen.blit(score_text, (4, game_config.get_window_height() - 39))
        self.draw_level_name(screen, level, color)

    def draw_level_name(self, screen, level, color):
        level_text = f"Fase Atual: {self.get_name_level(level)}"
        font_level_type = pg.font.SysFont("Comic Sans Ms", 17, True)
        font_level = font_level_type.render(level_text, True, color)
        screen.blit(font_level, (game_config.get_window_width() / 1.9, game_config.get_window_height() - 33))

    def get_name_level(self, level):
        if level == 1 or level == 2:
            return "Praça dos três poderes"
        elif level == 3:
            return "Orla de Icoaraci"
