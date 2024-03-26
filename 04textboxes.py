import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg 

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Setting the window title
        self.setWindowTitle("Hello World!")

        # Setting the layout to QVBoxLayout
        self.setLayout(qtw.QVBoxLayout())

        # Creating a label
        self.my_label = qtw.QLabel("Type something into this ")
        self.my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(self.my_label)

        # Creating the text box
        self.my_text = qtw.QTextEdit(self, lineWrapMode=qtw.QTextEdit.FixedColumnWidth, lineWrapColumnOrWidth=50, placeholderText="Hello World", readOnly=False)
        self.layout().addWidget(self.my_text)

        # Creating a button
        my_button = qtw.QPushButton("Press ME!")
        my_button.clicked.connect(self.press_it)  # Connect button clicked signal to press_it method
        self.layout().addWidget(my_button)

    def press_it(self):
        text = self.my_text.toPlainText()  # Get text from QTextEdit
        self.my_label.setText(f'You typed {text}')

# Create an application instance
app = qtw.QApplication([])

# Create and show the main window
window = MainWindow()
window.show()

# Run the application
app.exec_()





       
   


        

