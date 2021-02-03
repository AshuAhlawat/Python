import sys
import PyQt5.QtWidgets as qt

class Exampleapp(qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1300,560,550,500)
        self.setWindowTitle("Example")

app = qt.QApplication([])

window = Exampleapp()
window.show()

sys.exit(app.exec_())