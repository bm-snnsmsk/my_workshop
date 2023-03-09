import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QMainWindow) :
    count = 0
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QMdiSubWindow()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 800, 600)        
        self.initUI()

    def initUI(self) :
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File") ## ana menu
        file.addAction("New")  ## alt menü
        file.addAction("Cascade") ## alt menü
        file.addAction("Tiled") ## alt menü
        file.triggered[QAction].connect(self.WindowTrig)

    def WindowTrig(self, p) :
        if p.text() == "New" :
            MainWindow.count = MainWindow.count + 1 ## MainWindow, class adıyla aynı olmalı
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("new window : "+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()

        if p.text() == "Cascade" :
            self.mdi.cascadeSubWindows()

        if p.text() == "Tiled" :
            self.mdi.tileSubWindows()


def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
