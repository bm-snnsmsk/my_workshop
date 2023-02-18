import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip # bu satıra gerek olmaz ama yazım kolaylığı için 
from PyQt5.QtGui import QIcon

class MainForm(QMainWindow) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip("Calculator")
        self.initUI()
    
    def initUI(self) :
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayi1 : ")
        self.lbl_sayi1.move(50, 30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayi2 : ")
        self.lbl_sayi2.move(50, 60)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Sonuç : ") 
        self.lbl_result.resize(300,32)
        self.lbl_result.move(150, 190)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150, 30)   
        self.txt_sayi1.resize(100, 32)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150, 60)
        self.txt_sayi2.resize(100, 32)
        
        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150, 100)
        self.btn_topla.resize(50, 32)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(200, 100)
        self.btn_cikar.resize(50, 32)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(250, 100)
        self.btn_carp.resize(50, 32)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(300, 100)
        self.btn_bol.resize(50, 32)
        self.btn_bol.clicked.connect(self.hesapla)

    def hesapla(self) : 
        sender = self.sender().text()
        if sender == "Topla" :
            self.lbl_result.setText("Sonuç : "+ str(int(self.txt_sayi1.text()) + int(self.txt_sayi2.text()))) 
        elif sender == "Çıkar" :
            self.lbl_result.setText("Sonuç : "+ str(int(self.txt_sayi1.text()) - int(self.txt_sayi2.text()))) 
        elif sender  == "Çarp" :
            self.lbl_result.setText("Sonuç : "+ str(int(self.txt_sayi1.text()) * int(self.txt_sayi2.text()))) 
        elif sender  == "Böl" :
            self.lbl_result.setText("Sonuç : "+ str(int(self.txt_sayi1.text()) / int(self.txt_sayi2.text()))) 

 

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()

