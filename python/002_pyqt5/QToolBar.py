import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QMenuBar, QLabel, QAction
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainForm(QMainWindow) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QToolBar()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 500, 500)
        # self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
        # vbox = QVBoxLayout()

        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("File")
        editmenu = mainmenu.addMenu("Edit")
        viewmenu = mainmenu.addMenu("Edit")
        helpmenu = mainmenu.addMenu("Help")

        copyaction = QAction(QIcon("../images/icons/ok.ico"), "Copy", self)
        copyaction.setShortcut("Ctrl + C")
        filemenu.addAction(copyaction)

        cutaction = QAction(QIcon("../images/icons/red.ico"), "Cut", self)
        cutaction.setShortcut("Ctrl + X")
        filemenu.addAction(cutaction)

        saveaction = QAction(QIcon("../images/icons/blue.ico"), "Save", self)
        saveaction.setShortcut("Ctrl + S")
        filemenu.addAction(saveaction)

        exitaction = QAction(QIcon("../images/icons/close.ico"), "Exit", self)
        exitaction.setShortcut("Ctrl + E")
        exitaction.triggered.connect(self.exitWindow)
        editmenu.addAction(exitaction)

        toolbar = self.addToolBar("toolbar")
        toolbar.addAction(copyaction)
        toolbar.addAction(cutaction)
        toolbar.addAction(saveaction)
        toolbar.addAction(exitaction)
        


        # self.setLayout(vbox)


    def exitWindow(self) :
        self.close()
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
