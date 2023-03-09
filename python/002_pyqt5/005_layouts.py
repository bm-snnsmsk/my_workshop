import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGroupBox
from PyQt5.QtGui import QIcon, QPalette, QColor, QFont # QPalette = zemin rengi,

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

        # font = self.QtGui.QFont()
        # font.setPointSize(24)
        # font.setBold(True)
        # font.setWeight(75)

        # self.lbl_1.setFont(font)
        self.lbl_1 = QtWidgets.QLabel(self)
        self.lbl_1.setText("Layout")
        self.lbl_1.move(50, 30)

        
        

        vbox = QtWidgets.QVBoxLayout()  ## vertical
        self.layout = QtWidgets.QHBoxLayout()  ## horizontal


        self.layout.addWidget(self.lbl_1)
        self.layout.addWidget(Color("green"))
        self.layout.addWidget(Color("red"))
        self.layout.addWidget(Color("blue"))
        self.layout.addWidget(Color("gray"))
        self.layout.addWidget(Color("pink"))
        self.layout.addWidget(Color("yellow"))
        

        # widget = QWidget()
        # widget.setLayout(self.layout)
        # # widget = Color("blue")  ## widget'in arka planını belirlenen renge boyar
        # self.setCentralWidget(widget)
        # self.setCentralWidget(grpBox)


        grpBox = QGroupBox("Renkler")
        grpBox.setFont(QFont("Times News Roman", 15))

        grpBox.setLayout(self.layout)
        vbox.addWidget(grpBox)        
        self.setLayout(vbox)
        self.setCentralWidget(grpBox)


def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

