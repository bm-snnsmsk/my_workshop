import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, QSize


class MyWindow(QMainWindow) :
    def __init__(self) :
        super(MyWindow, self).__init__()
        self.setWindowTitle("ilk form uygulamam - 2 Class Uygulaması")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip("Class Uygulaması")
        self.initUI()
    
    def initUI(self) :
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("adınız : ")
        self.lbl_name.move(50, 30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız : ")
        self.lbl_surname.move(50, 60)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Sonuç : ") 
        self.lbl_result.resize(300,32)
        self.lbl_result.move(150, 190)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)   
        self.txt_name.resize(200, 32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150, 60)
        self.txt_surname.resize(200, 32)

        
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(150, 100)
        self.btn_save.clicked.connect(self.tikla)


        ###### Son eklemeler START ######################
        self.btn_yeni = QtWidgets.QPushButton("yeni",self)
        self.btn_yeni.setIcon(QIcon("green.ico"))
        self.btn_yeni.setIconSize(QSize(50,50)) ## w,h
        self.btn_yeni.setGeometry(QRect(150,250,100,75)) ## x,y,w,h
        ###### Son eklemeler START ######################


    

    def tikla(self) : 
        print("Merhaba "+ self.txt_name.text() + " " + self.txt_surname.text())
        self.lbl_result.setText("Sonuç : Merhaba "+ self.txt_name.text() + " " + self.txt_surname.text()) 

 

def window() :
    app = QApplication(sys.argv)
    win = MyWindow()
    

    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

