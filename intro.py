from PyQt5 import QtWidgets


from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(300,300,300,300)
    win.setWindowTitle("Hello world ")


    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())


window()

