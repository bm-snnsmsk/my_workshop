import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPalette, QColor # QPalette = zemin rengi, 

class Color(QWidget) :
    def __init__(self, color) :
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.setWindowTitle("Layouts")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip("Layouts")
        self.initUI()
    
    def initUI(self) :

        layout = QtWidgets.QGridLayout()

        layout.addWidget(Color("red"),0,0) ## vertical, horizontal
        layout.addWidget(Color("yellow"),1,0) ## vertical, horizontal
        layout.addWidget(Color("green"),4,2) ## vertical, horizontal
        layout.addWidget(Color("gray"),0,4) ## vertical, horizontal
        layout.addWidget(Color("pink"),2,2) ## vertical, horizontal
        layout.addWidget(Color("purple"),0,2) ## vertical, horizontal
        layout.addWidget(Color("purple"),3,3)
        layout.addWidget(Color("black"),2,4)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

 

def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

