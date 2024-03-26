import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World!")
        self.setLayout(qtw.QVBoxLayout())

        # Create the combo box
        my_combo = qtw.QComboBox(self)
        my_combo.addItem("Pepperoni", "Something")
        my_combo.addItem("Cheese", 2)
        my_combo.addItem("Mushroom", qtw.QWidget)
        my_combo.addItem("Peppers")
        self.layout().addWidget(my_combo)

        # Create a label
        my_label = qtw.QLabel("Pick something from here")
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create a button
        my_button = qtw.QPushButton("Press Me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        self .show()

        def press_it():
            # Adding something in the box
            # my_label.setText(f'You picked {my_combo.currentText()}!')
            my_label.setText(f'You picked {my_combo.currentIndex()}!')





app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

