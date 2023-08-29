from PyQt5 import QtCore, QtWidgets, QtGui


def groupbox_input_word(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    self.groupBox_input_word = QtWidgets.QGroupBox(Dialog)
    self.groupBox_input_word.setGeometry(QtCore.QRect(40, 90, 601, 431))
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(24)
    self.groupBox_input_word.setFont(font)
    self.groupBox_input_word.setStyleSheet(
        "color: white; background-color: #282836; border: 0px")
    self.groupBox_input_word.setStyle
    self.groupBox_input_word.setObjectName("groupBox_input_word")
    self.groupBox_input_word.setVisible(True)
    self.label_input_word_question = QtWidgets.QLabel(
        self.groupBox_input_word)
    self.label_input_word_question.setGeometry(
        QtCore.QRect(150, 110, 300, 61))
    self.label_input_word_question.setObjectName(
        "label_input_word_question")
    self.label_input_word_question.setFont(font)
    self.label_input_word_question.setStyleSheet(
        "color: black; background-color: transparent")
    self.pushButton_input_word_zatwierdz = QtWidgets.QPushButton(
        self.groupBox_input_word)
    self.pushButton_input_word_zatwierdz.setGeometry(
        QtCore.QRect(450, 370, 113, 32))
    self.pushButton_input_word_zatwierdz.setStyleSheet("QPushButton {\n"
                                                       "    color: black;\n"
                                                       "    font-size: 14px;\n"
                                                       "    border-radius: 10px;\n"
                                                       "    background: qradialgradient(\n"
                                                       "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                                       "        radius: 1.35, stop: 0 #fff, stop: 1 #3399FF\n"
                                                       "        );\n"
                                                       "    padding: 3px;\n"
                                                       "    }\n"
                                                       "\n"
                                                       "QPushButton:hover {\n"
                                                       "    background: qradialgradient(\n"
                                                       "        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
                                                       "        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
                                                       "        );\n"
                                                       "    }\n"
                                                       "\n"
                                                       "QPushButton:pressed {\n"
                                                       "    color: #0B5AE1;\n"
                                                       "    border-style: inset;\n"
                                                       "    background: #C5DEEB\n"
                                                       "    }")
    self.pushButton_input_word_zatwierdz.setObjectName(
        "pushButton_input_word_zatwierdz")
    self.linedit_given_word = QtWidgets.QLineEdit(self.groupBox_input_word)
    self.linedit_given_word.setGeometry(QtCore.QRect(60, 200, 471, 51))
    self.linedit_given_word.setObjectName(
        "linedit_given_word")
    self.pushButton_input_word_zatwierdz.clicked.connect(self.assignVariable)
    self.pushButton_input_word_zatwierdz.clicked.connect(
        self.hide_input_groupbox)
    self.pushButton_input_word_zatwierdz.setText(
        _translate("Dialog", "Zatwierdź"))
    self.label_input_word_question.setText(
        _translate("Dialog",  "<html><head/><body><p align=\"center\"><span style=\" color: white;\">Podaj hasło do zgadnięcia</span></p></body></html>"))

def hide_input_groupbox(self):
    self.groupBox_input_word.setVisible(False)