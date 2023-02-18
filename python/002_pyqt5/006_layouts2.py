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
        self.setGeometry(0, 0, 800, 800)
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setToolTip("Layouts")
        self.initUI()
    
    def initUI(self) :

        
        self.lbl_1 = QtWidgets.QLabel(self)
        self.lbl_1.setText("Layout")
        self.lbl_1.move(50, 30)

        self.hlayout1 = QtWidgets.QHBoxLayout()  ## horizontal
        self.hlayout2 = QtWidgets.QHBoxLayout()  ## horizontal
        self.vlayout1 = QtWidgets.QVBoxLayout()  ## vertical


        self.hlayout1.addWidget(self.lbl_1)
        self.hlayout1.addWidget(Color("green"))
        self.hlayout1.addWidget(Color("red"))
        self.hlayout1.addWidget(Color("blue"))
        self.hlayout1.setContentsMargins(50,100,150,200)  ## left, top, right, bottom
        self.hlayout1.setSpacing(50)  ## left, top, right, bottom

        self.hlayout2.addWidget(Color("gray"))
        self.hlayout2.addWidget(Color("pink"))
        self.hlayout2.addWidget(Color("yellow"))

        self.vlayout1.addLayout(self.hlayout1)
        self.vlayout1.addLayout(self.hlayout2)

        widget = QWidget()
        widget.setLayout(self.vlayout1)
        self.setCentralWidget(widget)

 

def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

