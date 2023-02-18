from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from untitled import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("İcon Yerleştirme")
        self.setStyleSheet("background-color:#3489ae; background-image:url('../images/1.jpg'); background-repeat: no-repeat;")
        # self.setWindowIcon(QIcon('icon.png'))
        self.setWindowIcon(QIcon(':/icon2/1.jpg'))
        
  

        self.ui.pushButton.setIcon(QIcon(":/icon/icon.png"))
        #self.pushButton.setIconSize(QtCore.QSize(64, 64))

      
   



   
   
    

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


