import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QProgressBar, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class MyThread(QThread) :
    change_value = pyqtSignal(int)
    def run(self) :
        cnt = 0 
        while cnt < 100 :
            cnt += 1
            time.sleep(0.3)
            self.change_value.emit(cnt) 

class MainForm(QDialog) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QProgressBar()")
        self.setGeometry(200, 200, 500, 100)
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()
        
        self.btn = QPushButton("Çalıştır")
        self.btn.setStyleSheet("background-color:yellow")
        self.btn.clicked.connect(self.startProgressbar)

        self.progressbar = QProgressBar()       
        self.progressbar.setMaximum(100)     
        self.progressbar.setOrientation(Qt.Vertical)    
        # self.progressbar.setTextVisible(False)    
        self.progressbar.setStyleSheet("QProgressBar {border:2px solid grey; border-radius:8px; padding:1px}" "QProgressBar::chunk {background-color:lightblue}")

        vbox.addWidget(self.progressbar)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

    def startProgressbar(self) :
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressValue)
        self.thread.start()

    def setProgressValue(self, val) :
        self.progressbar.setValue(val)

   

   
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
