from PyQt5 import QtCore, QtWidgets, QtGui


def show_brawo(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    self.label_brawo = QtWidgets.QLabel(Dialog)
    self.label_brawo.setGeometry(
        QtCore.QRect(180, 160, 330, 211))
    self.label_brawo.setObjectName(
        "label_guess_word")
    self.label_brawo.setFont(QtGui.QFont("Arial", 20))
    self.label_brawo.setAlignment(QtCore.Qt.AlignCenter)
    self.label_brawo.setText(_translate("Dialog", "Brawo! Zgadłeś"))
    self.label_brawo.setStyleSheet(
        "color: grey; background-color: white; border: 0px ")
    self.label_brawo.hide()
