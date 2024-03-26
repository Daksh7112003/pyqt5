import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
 def __init__(self):
  super().__init__()



  #add a title..


  self.setWindowTitle("hello world!!")



 # self.setLayout(qtw.QHBoxLayout())
  form_layout =qtw.QFormLayout()
  self.setLayout(form_layout)

   







  self.show()


app=qtw.QApplication([])
mw=MainWindow()
app.exec_()


