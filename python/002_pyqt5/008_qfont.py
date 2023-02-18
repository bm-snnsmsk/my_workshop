import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon

class MainForm(QMainWindow) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QFont()")
        self.setGeometry(200, 200, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))
        self.initUI()
    
    def initUI(self) :
        self.lbl_name = QLabel(self)
        self.lbl_name.setText("QFont ile yazı boyutu değiştirme")
        self.lbl_name.setFixedWidth(500)
        self.lbl_name.move(20,20)
        self.yazi_font = QFont()
        self.yazi_font.setFamily("Arial")
        self.yazi_font.setPointSize(16)
        self.lbl_name.setFont(self.yazi_font)
        self.txt = QLineEdit(self)
        self.txt.move(5,120)
        self.txtArea = QTextEdit(self)
        self.txtArea.move(5,250)

 

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

