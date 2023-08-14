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
