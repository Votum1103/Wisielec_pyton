from PyQt5 import QtCore, QtGui, QtWidgets


def multi_player_pushbutton(self, dialog_game):
    _translate = QtCore.QCoreApplication.translate
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(-1)
    font.setBold(True)
    font.setItalic(False)
    font.setUnderline(False)
    font.setWeight(75)
    self.pushButton_multiplayer = QtWidgets.QPushButton(dialog_game)
    self.pushButton_multiplayer.setGeometry(
        QtCore.QRect(220, 330, 251, 71))
    self.pushButton_multiplayer.setFont(font)
    self.pushButton_multiplayer.setMouseTracking(False)
    self.pushButton_multiplayer.setAutoFillBackground(False)
    self.pushButton_multiplayer.setStyleSheet("QPushButton {\n"
                                              "    color: #F27FFA;\n"
                                              "    text-align: right;\n"
                                              "    font-size: 18px;\n"
                                              "    border-radius: 10px;\n"
                                              "    background: qlineargradient(\n"
                                              "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #F27FFA,  stop: 0.3 #F27FFA\n"
                                              "        stop: 0.301 #FCFCFC, stop: 1 #FCFCFC\n"
                                              "        );\n"
                                              "    padding: 20px;\n"
                                              "    }\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    color: #FFFFFF;\n"
                                              "    background: qlineargradient(\n"
                                              "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #FCFCFC,  stop: 0.3 #FCFCFC\n"
                                              "        stop: 0.301 #F27FFA, stop: 1 #F27FFA\n"
                                              "        );\n"
                                              "    }\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    color: #E9AFEE;\n"
                                              "    border-style: inset;\n"
                                              "    background: qlineargradient(\n"
                                              "        x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 #E9AFEE,  stop: 0.3 #E9AFEE\n"
                                              "        stop: 0.301 #F9E8FA stop: 1 #F9E8FA\n"
                                              "        );\n"
                                              "    }")
    self.pushButton_multiplayer.setLocale(QtCore.QLocale(
        QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
    self.pushButton_multiplayer.setIconSize(QtCore.QSize(400, 400))
    self.pushButton_multiplayer.setObjectName("pushButton_multiplayer")
    self.pushButton_multiplayer.setText(
        _translate("dialog_game", "MULTIPLAYER"))
    self.label_multi_pict = QtWidgets.QLabel(dialog_game)
    self.label_multi_pict.setGeometry(QtCore.QRect(233, 350, 51, 31))
    self.label_multi_pict.setStyleSheet("background-color: transparent;")
    self.label_multi_pict.setText("")
    self.label_multi_pict.setPixmap(
        QtGui.QPixmap("images/mul.png"))
    self.label_multi_pict.setScaledContents(True)
    self.label_multi_pict.setObjectName("label_multi_pict")
