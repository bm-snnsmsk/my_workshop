import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon,  QPainter, QBrush, QPen, QLinearGradient
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPainter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
       
    
    def paintEvent(self, e) :
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine)) ## kenarlık

        grad1 = QLinearGradient(20,100,150,175)

        grad1.setColorAt(0.0, Qt.darkGray)
        grad1.setColorAt(0.5, Qt.green)
        grad1.setColorAt(1.0, Qt.yellow)

        painter.setBrush(QBrush(grad1))
        painter.drawRect(10,10,200,200)


        



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
