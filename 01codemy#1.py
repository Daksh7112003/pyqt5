import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg 




class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!!")

        self.setLayout(qtw.QVBoxLayout())  #QV for the vertical box and Qh for the horizontal box .....

        


        my_label = qtw.QLabel("hello world!")


# if we want to change the properties of label , then we have to import the gui systems....
        

        my_label.setFont(qtg.QFont('Helvetica' , 28))

        self.layout().addWidget(my_label)

        #Create an entry box ...

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)


        #CReate a button...

        my_button =qtw.QPushButton("Press Me!" ,clicked =lambda: press_it())
        self.layout().addWidget(my_button)


        #press_me fxn ...

        def press_it():

            #Adding something in the box..
            my_label.setText(f'Hello {my_entry.text()}')

            #Clearing the box...

            my_entry.setText("") 








        






















        self.show()




app =qtw.QApplication([])
mw =MainWindow()


app.exec_()


    