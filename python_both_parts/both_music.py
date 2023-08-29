from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


def play_music_in_game(self, Dialog):
    self.player = QMediaPlayer()
    url = QUrl.fromLocalFile("music/Happy.mp3")
    content = QMediaContent(url)
    self.player.setMedia(content)
    self.player.setVolume(5)
    self.player.play()


def play_music_after_getting_letter(self):
    self.player1 = QMediaPlayer()
    url = QUrl.fromLocalFile("music/When_you_get_letter.wav")
    content = QMediaContent(url)
    self.player1.setMedia(content)
    self.player1.setVolume(20)
    self.player1.play()
