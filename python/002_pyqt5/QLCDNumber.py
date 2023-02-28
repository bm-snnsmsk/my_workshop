import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from random import randint

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QLCDNumber()")
        self.setGeometry(200, 200, 500, 500)
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()
        
        self.btn = QPushButton("rastgele bir sayı seç")
        self.btn.setStyleSheet("background-color:yellow")
        self.btn.clicked.connect(self.LCDHandler)

        self.lcd = QLCDNumber()
        # self.lcd.display(60)
        self.lcd.setStyleSheet("background-color:green")
        


        vbox.addWidget(self.lcd)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

    def LCDHandler(self) :
        rnd_number = randint(1,200)
        self.lcd.display(rnd_number)

       
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
