from pygame import mixer


class Sound:
    def play_music_catch_cachaca(self, music_path, vol):
        mixer.init()
        mixer.Channel(0).set_volume(vol)
        mixer.Channel(0).play(mixer.Sound(music_path))

    def play_music_level(self, music_path, vol):
        mixer.init()
        mixer.init()
        mixer.Channel(1).set_volume(vol)
        mixer.Channel(1).play(mixer.Sound(music_path))