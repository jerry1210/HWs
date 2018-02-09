from task_4 import MusicFile


class TestMusicFile:

    def setup_method(self):
        self.music_file = MusicFile('.\\HW6\\music.txt')

    def test_artist(self):
        assert self.music_file.artist('Joy Division').songs == ['Love Will Tear Us Apart', 'New Dawn Fades']