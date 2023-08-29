from PyQt5 import QtCore, QtWidgets
from python_both_parts.both_letters_pushbuttons import push_button_style
from python_both_parts.both_guess_word_pushbutton import question_pushButton
from python_both_parts.both_word_displayed_label import (keyword_label,
                                                         addToWord)
from python_both_parts.both_guess_word_groupbox import (groupbox_guess_word,
                                                        show_groupbox,
                                                        hide_label,
                                                        try_to_guess)
from python_both_parts.both_szubienica_photos import zdj, show_wisielec
from python_both_parts.both_music import (play_music_in_game,
                                          play_music_after_getting_letter)
from python_both_parts.both_end_brawo_przegrales import show_brawo_przegrales
from python_both_parts.both_again_pushbutton import show_again_pushbutton
import random


class Ui_Dialog_single(object):
    def setupUi(self, Dialog_single):
        _translate = QtCore.QCoreApplication.translate
        self.multi = False
        Dialog_single.setObjectName("Dialog")
        Dialog_single.resize(677, 574)
        Dialog_single.setStyleSheet("background-color: white")
        Dialog_single.setWindowTitle(_translate("Dialog_single", "Wisielec"))
        self.addToWord = addToWord.__get__(self)
        self.show_groupbox = show_groupbox.__get__(self)
        self.try_to_guess = try_to_guess.__get__(self)
        self.hide_label = hide_label.__get__(self)
        self.show_wisielec = show_wisielec.__get__(self)
        self.play_music_after_getting_letter = play_music_after_getting_letter.__get__(
            self)
        question_pushButton(self, Dialog_single)
        question_pushButton(self, Dialog_single)
        keyword_label(self, Dialog_single)
        zdj(self, Dialog_single)
        push_button_style(self, Dialog_single)
        QtCore.QMetaObject.connectSlotsByName(Dialog_single)
        groupbox_guess_word(self, Dialog_single)
        self.photo_index = 0
        play_music_in_game(self, Dialog_single)
        show_brawo_przegrales(self, Dialog_single)
        show_again_pushbutton(self, Dialog_single)

    def assignVariableSingle(self):
        plik = "data/dane.txt"
        plik = open(plik, "r", encoding='utf8')
        words_from_file = plik.read().split(",")
        self.given_word = "".join(random.sample(
            words_from_file, 1)).strip().lower()
        self.word = "_ " * len(self.given_word)
        self.keyword_label.setText(self.word)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_single = QtWidgets.QDialog()
    ui = Ui_Dialog_single()
    ui.setupUi(Dialog_single)
    Dialog_single.show()
    ui.assignVariableSingle()
    sys.exit(app.exec_())
