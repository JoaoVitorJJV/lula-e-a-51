import pygame as pg
from src.components.entities.Lula import Player
from src.components.entities.Catch import Cachaca
from src.components.GUI import TextInterface
from src.components.Config import GameConfig
from src.components.SoundTracker import Sound
from src.components.entities.Enemy import BolsonaroEnemy
import os


game_config = GameConfig()

# background
bg = pg.image.load(os.path.join('src/img', 'background.jpg'))
screen = pg.display.set_mode(game_config.get_window_width_height())

# Sprites
player = Player()
cachaca = Cachaca()
bozonaro = BolsonaroEnemy()
group = pg.sprite.RenderPlain()
group.add(player)
group.add(cachaca)

# Text GUI
text_interface = TextInterface()


class Game:
    sound_played = 1
    level = 1

    def init_game(self, events):
        player_score = self.get_score()
        level = game_config.get_level()

        # Levels
        if level == 1:
            player.move()
            cachaca.check_colision(player.rect)
            screen.blit(bg, (0, 0))
            text_interface.draw_level_text(screen, level, "white")
            text_interface.draw_score(screen, level, "white")
            group.draw(screen)
            if player_score == 2 and self.sound_played == 1:
                self.play_sound_effect_level()
                self.sound_played += 1
                group.add(bozonaro)
                group.remove(cachaca)
                cachaca.kill()
                game_config.set_level(2)
        elif level == 2:
            if bozonaro.clicked:
                game_config.set_level(3)
                group.remove(bozonaro)
                bozonaro.kill()

            player.move()
            bozonaro.update(group, events)
            screen.blit(bg, (0, 0))
            text_interface.draw_level_text(screen, level, "white")
            text_interface.draw_score(screen, level, "white")
            group.draw(screen)

        elif level == 3:
            new_bg = pg.image.load(os.path.join('src/img', 'orla-de-icoaraci.jpg'))
            player.move()
            screen.blit(new_bg, (0, 0))
            text_interface.draw_level_text(screen, level, "black")
            text_interface.draw_score(screen, level, "black")
            group.draw(screen)

    def get_score(self):
        return player.score

    def play_sound_effect_level(self):
        sound = Sound()
        sound.play_music_level("src/sounds/success.mp3", 0.4)
