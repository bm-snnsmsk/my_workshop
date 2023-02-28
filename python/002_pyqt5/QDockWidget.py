import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QTextEdit, QDockWidget, QListWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QDockWidget()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
        self.initUI()

    def initUI(self) :
       menuBar = self.menuBar()
       file = menuBar.addMenu("File")
       file.addAction("New")
       file.addAction("Save")
       file.addAction("Close")

       self.dock = QDockWidget("Dockable Title", self)
       self.listWidget = QListWidget()

       list = ["python","c++","Java","c#"]
       self.listWidget.addItems(list)
       self.dock.setWidget(self.listWidget)

       self.setCentralWidget(QTextEdit())
       self.addDockWidget(Qt.RightDockWidgetArea, self.dock)





def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
