import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon,  QPainter, QBrush, QPen
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

        painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern)) ## içini doldurma
        painter.drawRect(10, 10, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern)) ## içini doldurma
        painter.drawRect(120, 10, 100, 100)

        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern)) ## içini doldurma
        painter.drawRect(230, 10, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern)) ## içini doldurma
        painter.drawRect(340, 10, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.HorPattern)) ## içini doldurma
        painter.drawRect(450, 10, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern)) ## içini doldurma
        painter.drawRect(10, 120, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.Dense3Pattern)) ## içini doldurma
        painter.drawRect(120, 120, 100, 100)
        
        painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern)) ## içini doldurma
        painter.drawRect(230, 120, 100, 100)



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
