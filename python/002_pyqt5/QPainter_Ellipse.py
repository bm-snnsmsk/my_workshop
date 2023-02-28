import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon,  QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPainter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 400)
       
    
    def paintEvent(self, e) :
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern)) ## içini doldurma
        painter.drawEllipse(100, 100, 400, 200)


def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
