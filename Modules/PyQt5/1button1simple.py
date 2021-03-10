from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def increment():
    global number
    number += 1
    num_label.setText(str(number))
    
number = 0 

# Window Setup
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(0,0, 1000,600)
win.setWindowTitle("Basic Button")

# Entities
num_label = QtWidgets.QLabel(win)
num_label.setText("0")
num_label.move(500,100)

num_button = QtWidgets.QPushButton(win)
num_button.setText("Click Me!")
num_button.move(500,400)
num_button.clicked.connect(increment)

win.show()
sys.exit(app.exec_())


