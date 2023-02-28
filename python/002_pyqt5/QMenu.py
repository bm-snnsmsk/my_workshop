import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainForm(QMainWindow) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QMenu()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 500, 500)
    
    def contextMenuEvent(self, event) :
        contextmenu = QMenu(self)
        newaction = contextmenu.addAction("New")
        openaction = contextmenu.addAction("Open")
        quitaction = contextmenu.addAction("Quit")

        action = contextmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitaction :
            self.close()
      
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
