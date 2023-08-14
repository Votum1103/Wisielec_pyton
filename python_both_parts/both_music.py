from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


def play_music_in_game(self, Dialog):
        self.player = QMediaPlayer()
        url = QUrl.fromLocalFile("Happy.mp3")
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.setVolume(5)
        self.player.play()
