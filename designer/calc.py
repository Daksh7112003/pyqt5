# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_label = QtWidgets.QLabel(self.centralwidget)
        self.output_label.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(34)
        self.output_label.setFont(font)
        self.output_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.output_label.setObjectName("output_label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget)
        self.seven_button.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiply_button.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget)
        self.nine_button.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget)
        self.eight_button.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtract_button.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.subtract_button.setFont(font)
        self.subtract_button.setObjectName("subtract_button")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.four_button = QtWidgets.QPushButton(self.centralwidget)
        self.four_button.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget)
        self.six_button.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget)
        self.five_button.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget)
        self.one_button.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setGeometry(QtCore.QRect(280, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget)
        self.three_button.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget)
        self.two_button.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.plusminus_button = QtWidgets.QPushButton(self.centralwidget)
        self.plusminus_button.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminus_button.setFont(font)
        self.plusminus_button.setObjectName("plusminus_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(280, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.decimal_button = QtWidgets.QPushButton(self.centralwidget)
        self.decimal_button.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget)
        self.zero_button.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        def press_it(self,pressed):
            self.outputLabel.setText(pressed)












    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.output_label.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "%"))
        self.pushButton_2.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "/"))
        self.pushButton_4.setText(_translate("MainWindow", "<<"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.multiply_button.setText(_translate("MainWindow", "*"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "X"))
        self.subtract_button.setText(_translate("MainWindow", "-"))
        self.pushButton_11.setText(_translate("MainWindow", "X"))
        self.pushButton_12.setText(_translate("MainWindow", "X"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.plusminus_button.setText(_translate("MainWindow", "+/-"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.zero_button.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
