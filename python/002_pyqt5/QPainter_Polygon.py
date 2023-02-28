import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon,  QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPainter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 400)
       
    
    def paintEvent(self, e) :  ## hazır fonksiyon
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine)) ## kenarlık
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern)) ## içini doldurur
        painter.setBrush(QBrush(Qt.blue, Qt.VerPattern)) ## içini doldurur
        painter.setBrush(QBrush(Qt.blue, Qt.HorPattern)) ## içini doldurur
        # point = ([
        #     QPoint(10,10),
        #     QPoint(10,100),
        #     QPoint(100,10),
        #     QPoint(100,100)
        # ])
        point = QPolygon([
            QPoint(10,10),
            QPoint(10,100),
            QPoint(100,10),
            QPoint(100,100)
        ])
        painter.drawPolygon(point)

def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
