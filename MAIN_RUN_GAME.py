from PyQt5 import QtWidgets
from initial_menu_all_in_one import Ui_dialog_game
from multi_all_in_one import Ui_Dialog_multi
from single_all_in_one import Ui_Dialog_single

class CommonWindow(QtWidgets.QDialog):
    def __init__(self, ui_class, open_function, stop_music_function):
        super().__init__()
        self.setupUi(self)
        if hasattr(self, 'play_again_pushbutton'):
            self.play_again_pushbutton.clicked.connect(self.open_window_from_this)
            self.play_again_pushbutton.clicked.connect(self.stop_music_after_click)
        self.ui_class = ui_class
        self.open_function = open_function
        self.stop_music_function = stop_music_function

    def open_window_from_this(self):
        self.hide()
        self.menu_window = self.open_function()
        self.menu_window.show()

    def stop_music_after_click(self):
        self.stop_music_function()

class FirstWindow(CommonWindow, Ui_dialog_game):
    def __init__(self):
        super().__init__(Ui_dialog_game, self.open_first_window, self.stop_music_after_click)

    def open_first_window(self):
        return FirstWindow()

class SecondWindow(CommonWindow, Ui_Dialog_multi):
    def __init__(self):
        super().__init__(Ui_Dialog_multi, self.open_first_window, self.stop_music_after_click)

class ThirdWindow(CommonWindow, Ui_Dialog_single):
    def __init__(self):
        super().__init__(Ui_Dialog_single, self.open_first_window, self.stop_music_after_click)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    firstWindow = FirstWindow()
    firstWindow.show()
    sys.exit(app.exec_())
