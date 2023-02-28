import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen, QTextDocument
from PyQt5.QtCore import Qt, QRectF

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPainter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
       
    
    def paintEvent(self, e) :
        painter = QPainter(self)

        painter.drawText(100, 100, "Sinan Şimşek")

        rect = QRectF(100,150,250,25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignCenter, "Hello QPainter")

        document = QTextDocument()
        rect2 = QRectF(0,0,500,250)
        document.setTextWidth(rect2.width())
        document.setHtml("<div><h2>HTML h2 TITLE </h2></div>  <b>Python GUI</b> <i>Development</i>")
        document.drawContents(painter, rect2)


        



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
