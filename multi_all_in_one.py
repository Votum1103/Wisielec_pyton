from PyQt5 import QtCore, QtWidgets
from python_both_parts.both_letters_pushbuttons import push_button_style
from python_both_parts.both_guess_word_pushbutton import question_pushButton
from python_both_parts.both_word_displayed_label import (keyword_label,
                                                         addToWord)
from python_multi_part.multi_input_word_groupbox import (groupbox_input_word,
                                                         hide_input_groupbox)
from python_both_parts.both_guess_word_groupbox import (groupbox_guess_word,
                                                        show_groupbox,
                                                        hide_label,
                                                        try_to_guess)
from python_both_parts.both_szubienica_photos import zdj, show_wisielec
from python_both_parts.both_music import (play_music_in_game,
                                          play_music_after_getting_letter)
from python_both_parts.both_end_brawo_przegrales import show_brawo_przegrales
from python_both_parts.both_again_pushbutton import show_again_pushbutton


class Ui_Dialog_multi(object):
    def setupUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.multi = True
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 574)
        Dialog.setStyleSheet("background-color: white")
        Dialog.setWindowTitle(_translate("Dialog", "Wisielec"))
        self.hide_input_groupbox = hide_input_groupbox.__get__(self)
        self.addToWord = addToWord.__get__(self)
        self.show_groupbox = show_groupbox.__get__(self)
        self.try_to_guess = try_to_guess.__get__(self)
        self.hide_label = hide_label.__get__(self)
        self.show_wisielec = show_wisielec.__get__(self)
        self.play_music_after_getting_letter = play_music_after_getting_letter.__get__(
            self)
        question_pushButton(self, Dialog)
        keyword_label(self, Dialog)
        zdj(self, Dialog)
        push_button_style(self, Dialog)
        groupbox_input_word(self, Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        groupbox_guess_word(self, Dialog)
        self.photo_index = 0
        play_music_in_game(self, Dialog)
        show_brawo_przegrales(self, Dialog)
        show_again_pushbutton(self, Dialog)

    def assignVariable(self):
        self.given_word = self.linedit_given_word.text()
        self.word = "_ " * len(self.given_word)
        for index, char in enumerate(self.given_word):
            if char == " ":
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    " " + self.word[index_space + 1:]
            elif char == "-":
                index_space = index * 2
                self.word = self.word[:index_space] + \
                    "-" + self.word[index_space + 1:]
        self.keyword_label.setText(self.word)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_multi()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
