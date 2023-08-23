from PyQt5 import QtCore, QtWidgets, QtGui


def show_brawo_przegrales(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    self.label_brawo = QtWidgets.QLabel(Dialog)
    self.label_brawo.setGeometry(
        QtCore.QRect(180, 160, 330, 211))
    self.label_brawo.setObjectName(
        "label_brawo")
    self.label_brawo.setFont(QtGui.QFont("Arial", 20))
    self.label_brawo.setAlignment(QtCore.Qt.AlignCenter)
    self.label_brawo.setText(_translate("Dialog", "Brawo! Zgadłeś"))
    self.label_brawo.setStyleSheet(
        "color: grey; background-color: white; border: 0px ")
    self.label_brawo.hide()
    self.label_przegrales = QtWidgets.QLabel(Dialog)
    self.label_przegrales.setGeometry(
        QtCore.QRect(180, 160, 330, 211))
    self.label_przegrales.setObjectName(
        "label_przegrales")
    self.label_przegrales.setFont(QtGui.QFont("Arial", 20))
    self.label_przegrales.setAlignment(QtCore.Qt.AlignCenter)
    self.label_przegrales.setStyleSheet(
        "color: grey; background-color: white; border: 0px ")
    self.label_przegrales.hide()
