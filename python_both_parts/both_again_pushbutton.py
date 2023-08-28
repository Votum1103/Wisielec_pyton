from PyQt5 import QtCore, QtWidgets, QtGui


def show_again_pushbutton(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    font = QtGui.QFont()
    font.setPointSize(-1)
    font.setBold(True)
    font.setWeight(75)
    self.play_again_pushbutton = QtWidgets.QPushButton(Dialog)
    self.play_again_pushbutton.setGeometry(QtCore.QRect(255, 310, 180, 31))
    self.play_again_pushbutton.setFont(font)
    self.play_again_pushbutton.setStyleSheet("QPushButton {\n"
                                             "    color: #565A5B;\n"
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
                                             "   background: #C5DEEB\n"
                                             "    }background-color:silver;")
    self.play_again_pushbutton.setObjectName("play_again_pushbutton")
    self.play_again_pushbutton.hide()
    self.play_again_pushbutton.setText(
        _translate("Dialog", "Zagraj jeszcze raz"))
