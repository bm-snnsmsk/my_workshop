import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt5.QtGui import QIcon, QBrush, QPainter, QPen
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QGraphicsView()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 400)
        self.initUI()
    
    def initUI(self) :
        self.scene = QGraphicsScene()
        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)

        self.pen = QPen(Qt.red)

        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(0,0,600,400)

        self.shapes()

    def shapes(self) :
        ellipse = self.scene.addEllipse(20,20,200,200,self.pen, self.greenBrush)
        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)
        rect = self.scene.addRect(-100,-100,200,200,self.pen, self.grayBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)


        



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
