import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


def window() :
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle("QWidget Örneği")
    win.setGeometry(0, 0, 500, 500)
    win.setWindowIcon(QIcon('icon.png'))
    win.setToolTip("QWidget Örneği")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("adınız : ")
    lbl_name.move(50, 30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız : ")
    lbl_surname.move(50, 60)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150, 30)    

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150, 60)

    def tikla(self) : 
        print("Merhaba "+ txt_name.text() + " " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150, 100)
    btn_save.clicked.connect(tikla)

   


    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

