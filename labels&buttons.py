import sys
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QLabel,QPushButton

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI')
        self.setGeometry(100, 100, 400, 300)

        # Create a label
        label_1 = QLabel('Our first label', self)
        label_1.move(50, 50)  # Move the label to (50, 50) position




        label_2=QLabel('Another label', self)


        label_2.move(50,100)




        button_1=QPushButton('click 1',self)
        button_2=QPushButton('click 2', self)


        button_1.move(200,50)
        button_2.move(200,100) 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec_())


        

    

    #we can also set the css of this , with the help of layout ....


    