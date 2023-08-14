from PyQt5 import QtCore, QtGui, QtWidgets


def connected_with_instruction(self, dialog_game):
    _translate = QtCore.QCoreApplication.translate
    font = QtGui.QFont()
    font.setFamily("Helvetica")
    font.setPointSize(-1)
    self.pushButton_instruction = QtWidgets.QPushButton(dialog_game)
    self.pushButton_instruction.setGeometry(
        QtCore.QRect(480, 480, 151, 41))
    self.pushButton_instruction.setFont(font)
    self.pushButton_instruction.setStyleSheet("QPushButton {\n"
                                              "    color: #565A5B;\n"
                                              "    border: 1px solid black;\n"
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
                                              "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                              "        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
                                              "        );\n"
                                              "    }\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    color: #0B5AE1;\n"
                                              "    border-style: inset;\n"
                                              "    background: #C5DEEB\n"
                                              "    }")
    self.pushButton_instruction.setObjectName("pushButton_instruction")
    self.pushButton_instruction.setText(
        _translate("dialog_game", "INSTRUKCJA"))
    self.pushButton_instruction.clicked.connect(self.print_instruction)
    self.groupBox_instruction = QtWidgets.QGroupBox(dialog_game)
    self.groupBox_instruction.setGeometry(QtCore.QRect(30, 170, 611, 400))
    font.setPointSize(18)
    self.groupBox_instruction.setFont(font)
    self.groupBox_instruction.setStyleSheet(
        "color: white; background-color: #282836;border: 0px ")
    self.groupBox_instruction.setObjectName("groupBox_instruction")
    self.groupBox_instruction.setVisible(False)
    self.textBrowser_instruction_text = QtWidgets.QTextBrowser(
        self.groupBox_instruction)
    self.textBrowser_instruction_text.setStyleSheet(
        "background-color: #282836;")
    self.textBrowser_instruction_text.setGeometry(
        QtCore.QRect(30, 30, 581, 240))
    self.textBrowser_instruction_text.setObjectName(
        "textBrowser_instruction_text")
    self.textBrowser_instruction_text.setHtml(_translate("dialog_game", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">1.  W grze multiplayer gracz pierwszy podaje słowo i przekazuje urządzenie graczowi drugiemu,  który zgaduje słowo wpisane przez gracza pierwszego. </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">2.  W grze singleplayer gracz zgaduje wymyślone przez komputer słowo. </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">3.  Definiowane słowa mogą składać się wyłącznie z liter,  spacji i myślników.   </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">4.  Słowa zgadujemy,  wciskając kolejno przyciski z literami.  </span></p>\n"
                                                         "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">5.  Jeśli domyślasz się,  jakie będzie słowo zanim zgadniesz wszystkie litery,  możesz podjąć próbę odgadnięcia go,  wciskając przycisk &quot;tak&quot; w polu &quot;Czy chcesz odgadnąć hasło&quot;,  a następnie wpisując słowo.  W razie nieudanej próby zostanie odjęte 5 pkt. </span></p></body></html>\n"
                                                        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#ffffff;\">6.  Gra kończy się,   gdy gracz zgadnie słowo bądź gdy zabraknie mu szansy na zgadnięcie kolejnych liter (gdy rysunek wisielca będzie już skońćzony).  </span></p>\n"))
    self.pushButton_instruction_wroc = QtWidgets.QPushButton(
        self.groupBox_instruction)
    self.pushButton_instruction_wroc.setGeometry(
        QtCore.QRect(460, 310, 151, 41))
    self.pushButton_instruction_wroc.setStyleSheet("QPushButton {\n"
                                                   "    color: #565A5B;\n"
                                                   "    border: 1px solid black;\n"
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
                                                   "        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
                                                   "        radius: 1.35, stop: 0 #fff, stop: 1 #A5E2FF\n"
                                                   "        );\n"
                                                   "    }\n"
                                                   "\n"
                                                   "QPushButton:pressed {\n"
                                                   "    color: #0B5AE1;\n"
                                                   "    border-style: inset;\n"
                                                   "    background: #C5DEEB\n"
                                                   "    }")
    self.pushButton_instruction_wroc.setObjectName(
        "pushButton_instruction_wroc")
    self.pushButton_instruction_wroc.setText(
        _translate("dialog_game", "WRÓĆ"))
    self.pushButton_instruction_wroc.clicked.connect(self.hide_instruction)
