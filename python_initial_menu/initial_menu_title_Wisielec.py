from PyQt5 import QtCore, QtWidgets, QtGui


def Wisielec_tittle(self, dialog_game):
    _translate = QtCore.QCoreApplication.translate
    font = QtGui.QFont()
    font.setFamily(".AppleSystemUIFont")
    font.setPointSize(45)
    font.setKerning(False)
    self.Wisielec_napis = QtWidgets.QLabel(dialog_game)
    self.Wisielec_napis.setGeometry(QtCore.QRect(250, 90, 300, 100))
    self.Wisielec_napis.setFont(font)
    self.Wisielec_napis.setStyleSheet("color: #0BAEF5;\n"
                                      "background-color:transparent;")
    self.Wisielec_napis.setObjectName("Wisielec_napis")
    self.Wisielec_napis.setText(_translate("dialog_game", "WISIELEC"))
