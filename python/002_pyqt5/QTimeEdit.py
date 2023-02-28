import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTimeEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QTimeEdit()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       time = QTime()
       time.setHMS(13,15,40)

       timeedit = QTimeEdit()
       timeedit.setFont(QFont("Sanserif", 15))
       timeedit.setTime(time)
       
       vbox.addWidget(timeedit)
       self.setLayout(vbox)




def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
