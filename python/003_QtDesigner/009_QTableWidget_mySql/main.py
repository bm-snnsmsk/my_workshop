from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from qtablewidget import Ui_MainWindow

import db


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        for i in db.getDatas() :
            print(i)
            print(db.getDatas())

        



   
    

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


