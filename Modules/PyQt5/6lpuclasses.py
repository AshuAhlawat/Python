from PyQt5 import QtCore, QtGui, QtWidgets
import os
import multiprocessing


def run(id_):
    os.system('python '+id_+'.py')
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 370)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.id_ = QtWidgets.QLineEdit(self.centralwidget)
        self.id_.setGeometry(QtCore.QRect(140, 30, 161, 31))
        self.id_.setObjectName("id_")
        
        self.pass_ = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_.setGeometry(QtCore.QRect(140, 90, 161, 31))
        self.pass_.setObjectName("pass_")
        
        self.microphone_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.microphone_btn.setGeometry(QtCore.QRect(360, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.microphone_btn.setFont(font)
        self.microphone_btn.setChecked(True)
        self.microphone_btn.setObjectName("microphone_btn")
        
        self.listen_only_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.listen_only_btn.setGeometry(QtCore.QRect(360, 86, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.listen_only_btn.setFont(font)
        self.listen_only_btn.setObjectName("listen_only_btn")
        
        self.start_class_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_class_btn.setGeometry(QtCore.QRect(160, 280, 161, 51))
        self.start_class_btn.setObjectName("start_class_btn")
        self.start_class_btn.clicked.connect(self.classes)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 476, 26))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LPU"))
        self.label.setText(_translate("MainWindow", "Reg No."))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.start_class_btn.setText(_translate("MainWindow", "Start"))
        self.microphone_btn.setText(_translate("MainWindow", "Microphone"))
        self.listen_only_btn.setText(_translate("MainWindow", "Listen Only"))
    
    def classes(self):
        if self.microphone_btn.isChecked():
            met = 0
        else:
            met = 1
            
        id_= self.id_.text()
        pass_ = self.pass_.text()
        
        if not id_:
            id_ = "12016043"
            pass_ = "SandyRuby@12"
            
        os.mkdir("./cache")        with open("./cache/"+id_+".py","w+") as f:
            f.write('''
button = "green"
poll = "B"

#you id below
id_ = "'''+str(id_)+'''"
# your password below
pass_ = "''' +str(pass_) +'''"

methods = ["Microphone","Listen only"]
method = methods['''+ str(met) +''']

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic":1,
})

driver = webdriver.Chrome(options=opt,executable_path="chromedriver.exe")

def onlineclassscript():

    driver.get("https://myclass.lpu.in")

    username = driver.find_element_by_name("i")
    username.send_keys(id_)
    password = driver.find_element_by_name("p")
    password.send_keys(pass_)
    password.send_keys(Keys.ENTER)

    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.LINK_TEXT, "View Classes/Meetings")
        )
    )

    search = driver.find_element_by_link_text("View Classes/Meetings")
    search.click()

    try:
        match_search = WebDriverWait(driver,20).until(
            expected_conditions.presence_of_element_located(
                (By.CLASS_NAME, "fc-content")
            )
        )
    except:
        quit()
    import time
    while True:
        try:
            time.sleep(1)
            search = driver.find_element_by_css_selector('a[style*="background: '+button+';"]')
            search.click()
            break
        except Exception as e:
            time.sleep(180)
            onlineclassscript()
    
    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[role="button"]')
        )
    )
    search = driver.find_element_by_css_selector('a[role="button"]')
    search.click()

    match_search = WebDriverWait(driver,400).until(
        expected_conditions.presence_of_element_located(
            (By.ID, 'frame')
        )
    )
    iframe = driver.find_element_by_id('frame')
    driver.switch_to.frame(iframe)

    match_search = WebDriverWait(driver,20).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[aria-label="' + method +'"]')
        )
    )
    search = driver.find_element_by_css_selector('button[aria-label="' + method +'"]')
    search.click()

    if method=="Microphone":
        match_search = WebDriverWait(driver,20).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[aria-label="Echo is audible"]')
            )
        )
        search = driver.find_element_by_css_selector('button[aria-label="Echo is audible"]')
        search.click()

    while True:
        try:
            match_search = WebDriverWait(driver,3).until(
                expected_conditions.presence_of_element_located(
                    (By.CSS_SELECTOR, 'button[aria-label="OK"]')
                )
            )
            onlineclassscript()
        except:
            try:
                match_search = WebDriverWait(driver,117).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div[class*="pollingContainer"]')
                    )
                )
                try:
                    search = driver.find_element_by_css_selector('button[aria-label="'+poll+'"]')
                    time.sleep(8)
                    search.click()
                except Exception as e:
                    search = driver.find_element_by_css_selector('button[aria-label="Yes"]')
                    time.sleep(5)
                    search.click()
            except Exception as e:
                pass

onlineclassscript()
''')
        p = multiprocessing.Process(target=run, args=[id_])
        p.start()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
