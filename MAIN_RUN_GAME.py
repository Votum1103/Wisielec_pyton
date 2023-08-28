from PyQt5 import QtWidgets
from initial_menu_all_in_one import Ui_dialog_game
from multi_all_in_one import Ui_Dialog_multi
from single_all_in_one import Ui_Dialog_single


class FirstWindow(QtWidgets.QDialog, Ui_dialog_game):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_singleplayer.clicked.connect(
            self.openThirdWindowFromSingle)
        self.pushButton_multiplayer.clicked.connect(
            self.openSecondWindowFromMulti)

    def openThirdWindowFromSingle(self):
        self.hide()
        self.singleWindow = ThirdWindow()
        self.singleWindow.show()
        self.singleWindow.assignVariableSingle()

    def openSecondWindowFromMulti(self):
        self.hide()
        self.multiWindow = SecondWindow()
        self.multiWindow.show()


class SecondWindow(QtWidgets.QDialog, Ui_Dialog_multi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def openFirstWindowFromSingle(self):
        self.hide()
        self.menuWindow = FirstWindow()
        self.menuWindow.show()


class ThirdWindow(QtWidgets.QDialog, Ui_Dialog_single):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.play_again_pushbutton.clicked.connect(
            self.openFirstWindowFromSingle)

    def openFirstWindowFromSingle(self):
        self.hide()
        self.menuWindow = FirstWindow()
        self.menuWindow.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstWindow = FirstWindow()
    firstWindow.show()
    sys.exit(app.exec_())
