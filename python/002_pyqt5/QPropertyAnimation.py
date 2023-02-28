import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPropertyAnimation()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
    
    def initUI(self) :
        self.button = QPushButton("Start",self)
        self.button.move(30,30)
        self.button.clicked.connect(self.doAnimation)

        self.frame = QFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(150,150,100,100)

    def doAnimation(self) :
        self.anim = QPropertyAnimation(self.frame, b"geometry")
        self.anim.setDuration(10000)
        self.anim.setStartValue(QRect(0,0,100,30))
        self.anim.setEndValue(QRect(250,250,100,30))
        self.anim.start()

        



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
