import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen, QConicalGradient
from PyQt5.QtCore import Qt, QPoint

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPainter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
       
    
    def paintEvent(self, e) :
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine)) ## kenarlık

        conicalgradient = QConicalGradient(QPoint(100,100), 10)

        conicalgradient.setColorAt(0.0, Qt.red)
        conicalgradient.setColorAt(0.8, Qt.green)
        conicalgradient.setColorAt(1.0, Qt.yellow)

        painter.setBrush(QBrush(conicalgradient))
        painter.drawRect(10,10,200,200)


        



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
