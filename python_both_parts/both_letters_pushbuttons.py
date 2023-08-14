from PyQt5 import QtCore, QtWidgets


def push_button_style(self, Dialog):
    _translate = QtCore.QCoreApplication.translate
    Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
    self.a_pushButton = QtWidgets.QPushButton(Dialog)
    self.aa_pushButton = QtWidgets.QPushButton(Dialog)
    self.b_pushButton = QtWidgets.QPushButton(Dialog)
    self.c_pushButton = QtWidgets.QPushButton(Dialog)
    self.cc_pushButton = QtWidgets.QPushButton(Dialog)
    self.d_pushButton = QtWidgets.QPushButton(Dialog)
    self.e_pushButton = QtWidgets.QPushButton(Dialog)
    self.ee_pushButton = QtWidgets.QPushButton(Dialog)
    self.f_pushButton = QtWidgets.QPushButton(Dialog)
    self.g_pushButton = QtWidgets.QPushButton(Dialog)
    self.h_pushButton = QtWidgets.QPushButton(Dialog)
    self.i_pushButton = QtWidgets.QPushButton(Dialog)
    self.j_pushButton = QtWidgets.QPushButton(Dialog)
    self.k_pushButton = QtWidgets.QPushButton(Dialog)
    self.l_pushButton = QtWidgets.QPushButton(Dialog)
    self.ll_pushButton = QtWidgets.QPushButton(Dialog)
    self.m_pushButton = QtWidgets.QPushButton(Dialog)
    self.n_pushButton = QtWidgets.QPushButton(Dialog)
    self.nn_pushButton = QtWidgets.QPushButton(Dialog)
    self.o_pushButton = QtWidgets.QPushButton(Dialog)
    self.oo_pushButton = QtWidgets.QPushButton(Dialog)
    self.p_pushButton = QtWidgets.QPushButton(Dialog)
    self.q_pushButton = QtWidgets.QPushButton(Dialog)
    self.r_pushButton = QtWidgets.QPushButton(Dialog)
    self.s_pushButton = QtWidgets.QPushButton(Dialog)
    self.ss_pushButton = QtWidgets.QPushButton(Dialog)
    self.t_pushButton = QtWidgets.QPushButton(Dialog)
    self.u_pushButton = QtWidgets.QPushButton(Dialog)
    self.w_pushButton = QtWidgets.QPushButton(Dialog)
    self.x_pushButton = QtWidgets.QPushButton(Dialog)
    self.y_pushButton = QtWidgets.QPushButton(Dialog)
    self.z_pushButton = QtWidgets.QPushButton(Dialog)
    self.zz_pushButton = QtWidgets.QPushButton(Dialog)
    self.zzz_pushButton = QtWidgets.QPushButton(Dialog)
    self.button_names = [[self.a_pushButton, "a", "a", "A"],
                         [self.aa_pushButton, "aa", "ą", "Ą"],
                         [self.b_pushButton, "b", "b", "B"],
                         [self.c_pushButton, "c", "c", "C"],
                         [self.cc_pushButton, "cc", "ć", "Ć"],
                         [self.d_pushButton, "d", "d", "D"],
                         [self.e_pushButton, "e", "e", "E"],
                         [self.ee_pushButton, "ee", "ę", "Ę"],
                         [self.f_pushButton, "f", "f", "F"],
                         [self.g_pushButton, "g", "g", "G"],
                         [self.h_pushButton, "h", "h", "H"],
                         [self.i_pushButton, "i", "i", "I"],
                         [self.j_pushButton, "j", "j", "J"],
                         [self.k_pushButton, "k", "k", "K"],
                         [self.l_pushButton, "l", "l", "L"],
                         [self.ll_pushButton, "ll", "ł", "Ł"],
                         [self.m_pushButton, "m", "m", "M"],
                         [self.n_pushButton, "n", "n", "N"],
                         [self.nn_pushButton, "nn", "ń", "Ń"],
                         [self.o_pushButton, "o", "o", "O"],
                         [self.oo_pushButton, "oo", "ó", "Ó"],
                         [self.p_pushButton, "p", "p", "P"],
                         [self.q_pushButton, "q", "q", "Q"],
                         [self.r_pushButton, "r", "r", "R"],
                         [self.s_pushButton, "s", "s", "S"],
                         [self.ss_pushButton, "ss", "ś", "Ś"],
                         [self.t_pushButton, "t", "t", "T"],
                         [self.u_pushButton, "u", "u", "U"],
                         [self.w_pushButton, "w", "w", "W"],
                         [self.x_pushButton, "x", "x", "X"],
                         [self.y_pushButton, "y", "y", "Y"],
                         [self.z_pushButton, "z", "z", "Z"],
                         [self.zz_pushButton, "zz", "ź", "Ź"],
                         [self.zzz_pushButton, "zzz", "ż", "Ż"]]
    for index, list in enumerate(self.button_names):
        if index < 17:
            list[0].setGeometry(QtCore.QRect(90 + 30 * index, 410, 21, 28))
        elif index >= 17:
            list[0].setGeometry(QtCore.QRect(
                90 + 30 * (index-17), 450, 21, 28))
        list[0].setStyleSheet("QPushButton {\n"
                              "     border-radius: 10px;\n"
                              "     background-color: grey;\n"
                              "     color: white;\n"
                              "     font-size: 16px;\n"
                              "}\n"
                              "\n"
                              "QPushButton:hover {\n"
                              "     background-color: #C0C0C0;\n"
                              "     color: yellow\n"
                              "}\n"
                              "QPushButton:pressed {\n"
                              "     background-color: #A9A9A9;\n"
                              "}")
        list[0].setObjectName(f"{list[1]}_pushButton")
        list[0].setText(_translate("Dialog", list[3]))
        list[0].clicked.connect(lambda _, l=list[2]: self.addToWord(l))
        list[0].clicked.connect(
            lambda _, button=list[0]: button.setVisible(False))
        list[0].clicked.connect(lambda _, l=list[2]: self.show_wisielec(l))
        list[0].clicked.connect(self.play_music_after_getting_letter)
