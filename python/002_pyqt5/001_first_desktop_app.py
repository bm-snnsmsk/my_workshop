import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5 import QtGui


def window() :
    #app = QtWidgets.QApplication(sys.argv) 
    app = QApplication(sys.argv)   # from PyQt5.QtWidgets import QApplication, QMainWindow yazıldığından

    win = QMainWindow()
    win.setWindowTitle("ilk form uygulamam")
    win.setGeometry(0, 0, 500, 500)
    win.setWindowIcon(QtGui.QIcon('icon.jpg'))
    win.setToolTip("ilk masaüstü uygulamam")

    win.show()
    sys.exit(app.exec_())  # hemen değil x butonuna basıldığında kapanması için

window()

