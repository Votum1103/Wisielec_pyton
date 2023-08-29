from PyQt5 import QtCore, QtGui, QtWidgets


def keyword_label(self, Dialog):
    """odpowiada za wyświetlanie zgadywanego słowa
    (kresek odpowiadających za niezgadnięte litery i zgadnięte litery)"""
    font = QtGui.QFont()
    font.setPointSize(24)
    font.setBold(True)
    font.setWeight(75)
    self.keyword_label = QtWidgets.QLabel(Dialog)
    self.keyword_label.setGeometry(QtCore.QRect(70, 80, 551, 41))
    self.keyword_label.setFont(font)
    self.keyword_label.setStyleSheet(
        "color: grey; background-color:transparent;")
    self.keyword_label.setAlignment(QtCore.Qt.AlignCenter)
    self.keyword_label.setObjectName("keyword_label")


def addToWord(self, letter):
    for index, char in enumerate(self.given_word):
        if char == letter.lower() or char == letter.capitalize():
            index_space = index * 2
            self.word = self.word[:index_space] + \
                letter.capitalize() + self.word[index_space + 1:]
            self.keyword_label.setText(self.word)
        if self.word.capitalize().replace(" ", "") == self.given_word.capitalize().replace(" ", ""):
            self.label_brawo.show()
            self.play_again_pushbutton.show()
            self.question_pushButton.setEnabled(False)
            for list in self.button_names:
                list[0].setEnabled(False)
