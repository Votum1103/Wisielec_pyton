from PyQt5 import QtCore, QtGui, QtWidgets


def single_player_pushbutton(self, dialog_game):
    _translate = QtCore.QCoreApplication.translate
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(-1)
    font.setBold(True)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(75)
    self.pushButton_singleplayer = QtWidgets.QPushButton(dialog_game)
    self.pushButton_singleplayer.setGeometry(
        QtCore.QRect(220, 230, 251, 71))
    self.pushButton_singleplayer.setFont(font)
    self.pushButton_singleplayer.setMouseTracking(False)
    self.pushButton_singleplayer.setAutoFillBackground(False)
    self.pushButton_singleplayer.setStyleSheet("QPushButton {\n"
                                               "    color: #0BAEF5;\n"
                                               "    font-size: 18px;\n"
                                               "    text-align: right;\n"
                                               "    border-radius: 10px;\n"
                                               "    background: qlineargradient(\n"
                                               "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #0BAEF5  stop: 0.3 #0BAEF5\n"
                                               "        stop: 0.301 #FCFCFC, stop: 1 #FCFCFC\n"
                                               "        );\n"
                                               "    padding: 20px;\n"
                                               "    }\n"
                                               "\n"
                                               "QPushButton:hover {\n"
                                               "    color: #FFFFFF;\n"
                                               "    background: qlineargradient(\n"
                                               "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #FCFCFC,  stop: 0.3 #FCFCFC\n"
                                               "        stop: 0.301 #0BAEF5, stop: 1 #0BAEF5\n"
                                               "        );\n"
                                               "    }\n"
                                               "\n"
                                               "QPushButton:pressed {\n"
                                               "    color: #6CBAD2;\n"
                                               "    border-style: inset;\n"
                                               "    background: qlineargradient(\n"
                                               "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #6CBAD2,  stop: 0.3 #6CBAD2\n"
                                               "        stop: 0.301 #EFFCFF stop: 1 #EFFCFF\n"
                                               "        );\n"
                                               "    }")
    self.pushButton_singleplayer.setLocale(QtCore.QLocale(
        QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
    self.pushButton_singleplayer.setIconSize(QtCore.QSize(400, 400))
    self.pushButton_singleplayer.setObjectName("pushButton_singleplayer")
    self.pushButton_singleplayer.setText(
        _translate("dialog_game", "SINGLEPLAYER"))
    self.label_single_pict = QtWidgets.QLabel(dialog_game)
    self.label_single_pict.setGeometry(QtCore.QRect(237, 235, 41, 51))
    self.label_single_pict.setStyleSheet("background-color: transparent;")
    self.label_single_pict.setText("")
    self.label_single_pict.setPixmap(
        QtGui.QPixmap("images/sing.png"))
    self.label_single_pict.setScaledContents(True)
    self.label_single_pict.setObjectName("label_single_pict")
