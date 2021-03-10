from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.number = 0
        
        self.setGeometry(0,0, 1000,600)
        self.setWindowTitle("Basic Button")

        self.num_label = QtWidgets.QLabel(self)
        self.num_label.setText("0")
        self.num_label.move(500,100)

        self.num_button = QtWidgets.QPushButton(self)
        self.num_button.setText("Click Me!")
        self.num_button.move(500,400)
        self.num_button.clicked.connect(self.increment)
    
    def increment(self):
        self.number += 1
        self.num_label.setText(str(self.number))

# Window Setup
app = QApplication(sys.argv)
win = Window()

win.show()
sys.exit(app.exec_())

