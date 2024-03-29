# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '4calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # logic
        self.brac_start = 0
        self.display_text = ""
        
        #main window setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 722)
        MainWindow.setStyleSheet("background-color:rgb(60,60,60);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 0, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:rgb(30,0,40);color:white;border-bottom:4px solid white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 80, 431, 591))
        self.frame.setStyleSheet("margin:6;border-radius:10px;background-color:rgb(60,60,60);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        
        
                                    # Buttons
                                    
                                    
                                    
        self.remainder = QtWidgets.QPushButton(self.frame)
        self.remainder.setGeometry(QtCore.QRect(0, 0, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.remainder.setFont(font)
        self.remainder.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.remainder.setObjectName("remainder")
        
        self.clear_all = QtWidgets.QPushButton(self.frame)
        self.clear_all.setGeometry(QtCore.QRect(110, 0, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.clear_all.setFont(font)
        self.clear_all.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.clear_all.setObjectName("clear_all")
        
        self.clear = QtWidgets.QPushButton(self.frame)
        self.clear.setGeometry(QtCore.QRect(220, 0, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.clear.setFont(font)
        self.clear.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.clear.setObjectName("clear")
        
        self.backspace = QtWidgets.QPushButton(self.frame)
        self.backspace.setGeometry(QtCore.QRect(330, 0, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.backspace.setFont(font)
        self.backspace.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.backspace.setObjectName("backspace")
        
        self.root = QtWidgets.QPushButton(self.frame)
        self.root.setGeometry(QtCore.QRect(220, 100, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.root.setFont(font)
        self.root.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.root.setObjectName("root")
        
        self.reciprocal = QtWidgets.QPushButton(self.frame)
        self.reciprocal.setGeometry(QtCore.QRect(0, 100, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.reciprocal.setFont(font)
        self.reciprocal.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.reciprocal.setObjectName("reciprocal")
        
        self.power = QtWidgets.QPushButton(self.frame)
        self.power.setGeometry(QtCore.QRect(110, 100, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        self.power.setFont(font)
        self.power.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.power.setObjectName("power")
        
        self.divide = QtWidgets.QPushButton(self.frame)
        self.divide.setGeometry(QtCore.QRect(330, 100, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(18)
        self.divide.setFont(font)
        self.divide.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.divide.setObjectName("divide")
        
        self.b9 = QtWidgets.QPushButton(self.frame)
        self.b9.setGeometry(QtCore.QRect(220, 200, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b9.setFont(font)
        self.b9.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b9.setObjectName("b9")
        
        self.b7 = QtWidgets.QPushButton(self.frame)
        self.b7.setGeometry(QtCore.QRect(0, 200, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b7.setFont(font)
        self.b7.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b7.setObjectName("b7")
        
        self.b8 = QtWidgets.QPushButton(self.frame)
        self.b8.setGeometry(QtCore.QRect(110, 200, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b8.setFont(font)
        self.b8.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b8.setObjectName("b8")
        
        self.multiply = QtWidgets.QPushButton(self.frame)
        self.multiply.setGeometry(QtCore.QRect(330, 200, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        self.multiply.setFont(font)
        self.multiply.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.multiply.setObjectName("multiply")
        
        self.b6 = QtWidgets.QPushButton(self.frame)
        self.b6.setGeometry(QtCore.QRect(220, 300, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b6.setFont(font)
        self.b6.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b6.setObjectName("b6")
        
        self.b4 = QtWidgets.QPushButton(self.frame)
        self.b4.setGeometry(QtCore.QRect(0, 300, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b4.setFont(font)
        self.b4.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b4.setObjectName("b4")
        
        self.b5 = QtWidgets.QPushButton(self.frame)
        self.b5.setGeometry(QtCore.QRect(110, 300, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b5.setFont(font)
        self.b5.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b5.setObjectName("b5")
        
        self.minus = QtWidgets.QPushButton(self.frame)
        self.minus.setGeometry(QtCore.QRect(330, 300, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        self.minus.setFont(font)
        self.minus.setStyleSheet("background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;")
        self.minus.setObjectName("minus")
        
        self.b3 = QtWidgets.QPushButton(self.frame)
        self.b3.setGeometry(QtCore.QRect(220, 400, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b3.setFont(font)
        self.b3.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b3.setObjectName("b3")
        
        self.b1 = QtWidgets.QPushButton(self.frame)
        self.b1.setGeometry(QtCore.QRect(0, 400, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b1.setObjectName("b1")
        
        self.b2 = QtWidgets.QPushButton(self.frame)
        self.b2.setGeometry(QtCore.QRect(110, 400, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b2.setFont(font)
        self.b2.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b2.setObjectName("b2")
        
        self.plus = QtWidgets.QPushButton(self.frame)
        self.plus.setGeometry(QtCore.QRect(330, 400, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.plus.setFont(font)
        self.plus.setStyleSheet("background-color:rgb(30,30,30);  color:white;  background-color:rgb(30,30,30);  color:rgb(200,200,200);  border-radius:10px;-radius:10px;")
        self.plus.setObjectName("plus")
        
        self.point = QtWidgets.QPushButton(self.frame)
        self.point.setGeometry(QtCore.QRect(220, 500, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        self.point.setFont(font)
        self.point.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.point.setObjectName("point")
        
        self.bracket = QtWidgets.QPushButton(self.frame)
        self.bracket.setGeometry(QtCore.QRect(0, 500, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.bracket.setFont(font)
        self.bracket.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.bracket.setObjectName("sign")
        
        self.b0 = QtWidgets.QPushButton(self.frame)
        self.b0.setGeometry(QtCore.QRect(110, 500, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.b0.setFont(font)
        self.b0.setStyleSheet("background-color:rgb(30,30,50);  color:white;  border-radius:10px;")
        self.b0.setObjectName("b0")
        
        self.equal = QtWidgets.QPushButton(self.frame)
        self.equal.setGeometry(QtCore.QRect(330, 500, 101, 91))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(22)
        self.equal.setFont(font)
        self.equal.setStyleSheet("background-color:rgb(150,40,40);  color:rgb(200,200,200);  border-radius:10px;border: 5px solid white;")
        self.equal.setObjectName("bracket")
        
        self.history = QtWidgets.QLabel(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(440, 80, 261, 591))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        self.history.setFont(font)
        self.history.setStyleSheet("background-color:rgb(45,40,40);color:rgb(200,200,200);border:2px solid white;")
        self.history.setText("")
        self.history.setScaledContents(True)
        self.history.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.history.setWordWrap(True)
        self.history.setObjectName("history")
        
        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setGeometry(QtCore.QRect(0, 0, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.display.setFont(font)
        self.display.setAutoFillBackground(False)
        self.display.setStyleSheet("background-color:rgb(30,0,40);  color:white;  border-radius:10px;")
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        
        
        self.minus.clicked.connect(self.minus_click)
        self.plus.clicked.connect(self.plus_click)
        self.multiply.clicked.connect(self.multiply_click)
        self.divide.clicked.connect(self.divide_click)
        self.power.clicked.connect(self.power_click)
        self.root.clicked.connect(self.root_click)
        self.clear.clicked.connect(self.clear_click)
        self.clear_all.clicked.connect(self.clear_all_click)
        self.remainder.clicked.connect(self.remainder_click)
        self.reciprocal.clicked.connect(self.reciprocal_click)
        
        self.b0.clicked.connect(self.b0_click)
        self.b1.clicked.connect(self.b1_click)
        self.b2.clicked.connect(self.b2_click)
        self.b3.clicked.connect(self.b3_click)
        self.b4.clicked.connect(self.b4_click)
        self.b5.clicked.connect(self.b5_click)
        self.b6.clicked.connect(self.b6_click)
        self.b7.clicked.connect(self.b7_click)
        self.b8.clicked.connect(self.b8_click)
        self.b9.clicked.connect(self.b9_click)
        
        self.backspace.clicked.connect(self.backspace_click)
        self.bracket.clicked.connect(self.bracket_click)
        self.equal.clicked.connect(self.equal_click)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.label_2.setText(_translate("MainWindow", "History"))
        
        self.remainder.setText(_translate("MainWindow", "%"))
        self.clear_all.setText(_translate("MainWindow", "CE"))
        self.clear.setText(_translate("MainWindow", "C"))
        self.backspace.setText(_translate("MainWindow", "<<"))
        self.root.setText(_translate("MainWindow", "**-"))
        self.reciprocal.setText(_translate("MainWindow", "1/x"))
        self.power.setText(_translate("MainWindow", "**"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.minus.setText(_translate("MainWindow", "-"))
        
        self.b9.setText(_translate("MainWindow", "9"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.b0.setText(_translate("MainWindow", "0"))
        self.b2.setText(_translate("MainWindow", "2"))
        
        self.bracket.setText(_translate("MainWindow", "("))
        self.plus.setText(_translate("MainWindow", "+"))
        self.point.setText(_translate("MainWindow", "."))
        self.equal.setText(_translate("MainWindow", "="))
        self.display.setText(_translate("MainWindow", ""))

    def remainder_click(self):
        self.display_text += "%"
        self.display.setText(self.display_text)
    def point_click(self):
        self.display_text += "."
        self.display.setText(self.display_text)
    def plus_click(self):
        self.display_text += "+"
        self.display.setText(self.display_text)
    def minus_click(self):
        self.display_text += "-"
        self.display.setText(self.display_text)
    def multiply_click(self):
        self.display_text += "*"
        self.display.setText(self.display_text)
    def divide_click(self):
        self.display_text += "/"
        self.display.setText(self.display_text)
    def power_click(self):
        self.display_text += "**"
        self.display.setText(self.display_text)
    def root_click(self):
        self.display_text += "**-"
        self.display.setText(self.display_text)
    def reciprocal_click(self):
        self.display_text =  "1/"+self.display_text
        self.display.setText(self.display_text)
        
        
    def b9_click(self):
        self.display_text += "9"
        self.display.setText(self.display_text)
    def b8_click(self):
        self.display_text += "8"
        self.display.setText(self.display_text)
    def b7_click(self):
        self.display_text += "7"
        self.display.setText(self.display_text)
    def b6_click(self):
        self.display_text += "6"
        self.display.setText(self.display_text)
    def b5_click(self):
        self.display_text += "5"
        self.display.setText(self.display_text)
    def b4_click(self):
        self.display_text += "4"
        self.display.setText(self.display_text)
    def b3_click(self):
        self.display_text += "3"
        self.display.setText(self.display_text)
    def b2_click(self):
        self.display_text += "2"
        self.display.setText(self.display_text)
    def b1_click(self):
        self.display_text += "1"
        self.display.setText(self.display_text)
    def b0_click(self):
        self.display_text +=  "0"
        self.display.setText(self.display_text)
        
        
    def clear_click(self):
        self.display_text = ""
        self.display.setText(self.display_text)
    def clear_all_click(self):
        self.display_text = ""
        self.display.setText(self.display_text)
        self.history.setText("")
    def bracket_click(self):
        if self.brac_start:
            self.bracket.setText("(")
            self.display_text += ")"
            self.display.setText(self.display_text)
            self.brac_start=0
        else:
            self.bracket.setText(")")
            self.display_text += "("
            self.display.setText(self.display_text)
            self.brac_start=1
    def equal_click(self):
        try:
            answer = str(eval(self.display_text))
            self.display.setText(answer)
            self.history.setText(self.history.text()+ "\n" +self.display_text + " = " + answer)
        except:
            self.display.setText("WRONG INPUT")
        finally:
            self.display_text = ""
    def backspace_click(self):
        if self.display_text:
            self.display_text = str(self.display.text())
            self.display_text = self.display_text.replace(self.display_text[len(self.display_text)-1], "")
            self.display.setText(self.display_text)
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
