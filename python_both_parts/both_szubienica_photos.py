from PyQt5 import QtCore, QtGui, QtWidgets


def zdj(self, Dialog):
    self.szub1_label = QtWidgets.QLabel(Dialog)
    self.szub2_label = QtWidgets.QLabel(Dialog)
    self.szub3_label = QtWidgets.QLabel(Dialog)
    self.szub4_label = QtWidgets.QLabel(Dialog)
    self.szub5_label = QtWidgets.QLabel(Dialog)
    self.szub6_label = QtWidgets.QLabel(Dialog)
    self.szub7_label = QtWidgets.QLabel(Dialog)
    self.szub8_label = QtWidgets.QLabel(Dialog)
    self.szub9_label = QtWidgets.QLabel(Dialog)
    self.szub10_label = QtWidgets.QLabel(Dialog)
    self.szub11_label = QtWidgets.QLabel(Dialog)
    zdj_names = [[self.szub1_label, "images/szub0.png"],
                 [self.szub2_label, "images/szub1.png"],
                 [self.szub3_label, "images/szub2.png"],
                 [self.szub4_label, "images/szub3.png"],
                 [self.szub5_label, "images/szub4.png"],
                 [self.szub6_label, "images/szub5.png"],
                 [self.szub7_label, "images/szub6.png"],
                 [self.szub8_label, "images/szub7.png"],
                 [self.szub9_label, "images/szub8.png"],
                 [self.szub10_label, "images/szub9.png"],
                 [self.szub11_label, "images/szub10.png"]]
    for list in zdj_names:
        list[0].setGeometry(QtCore.QRect(230, 160, 200, 200))
        list[0].setStyleSheet("background-color:transparent;")
        list[0].setPixmap(QtGui.QPixmap(list[1]))
        list[0].setScaledContents(True)
        list[0].setVisible(False)


def show_wisielec(self, letter):
    _translate = QtCore.QCoreApplication.translate
    photos = [self.szub1_label,
              self.szub2_label,
              self.szub3_label,
              self.szub4_label,
              self.szub5_label,
              self.szub6_label,
              self.szub7_label,
              self.szub8_label,
              self.szub9_label,
              self.szub10_label,
              self.szub11_label]
    if self.photo_index == 0 and letter.lower() not in self.given_word:
        photos[self.photo_index].setVisible(True)
        self.photo_index += 1
    elif letter.lower() not in self.given_word and self.photo_index < 11:
        photos[self.photo_index-1].setVisible(False)
        photos[self.photo_index].setVisible(True)
        self.photo_index += 1
    elif letter.lower() not in self.given_word and self.photo_index == 11:
        photos[self.photo_index-1].setVisible(False)
        self.label_przegrales.show()
        self.play_again_pushbutton.show()
        self.label_przegrales.setText(_translate(
            "Dialog", f"Przegrałeś\n hasło to: {self.given_word.upper()}"))
        self.question_pushButton.setEnabled(False)
        for list in self.button_names:
            list[0].setEnabled(False)
