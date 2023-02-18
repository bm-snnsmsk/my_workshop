import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

def window() :
    #app = QtWidgets.QApplication(sys.argv)
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.show()
    sys.exit(app.exec_())
window()
