import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QToolBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QToolBox()")
        self.setGeometry(200, 200, 500, 500)
        self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()

        toolbox = QToolBox()
        toolbox.setStyleSheet("background-color:green")
        
        label = QLabel()
        toolbox.addItem(label, "Python")
        
        label = QLabel()
        toolbox.addItem(label, "Java")
        
        label = QLabel()
        toolbox.addItem(label, "C++")


        vbox.addWidget(toolbox)
        self.setLayout(vbox)


       
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
