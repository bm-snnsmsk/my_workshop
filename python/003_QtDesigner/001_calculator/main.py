from PyQt5 import QtWidgets
import sys
from calculator import Ui_MainWindow



class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_topla.clicked.connect(self.hesapla)
        self.ui.btn_cikar.clicked.connect(self.hesapla)
        self.ui.btn_carp.clicked.connect(self.hesapla)
        self.ui.btn_bol.clicked.connect(self.hesapla)
        self.setWindowTitle("denememeeee")
        self.ui.centralwidget.setStyleSheet("background-color:#125789;  ")
        self.ui.btn_topla.setStyleSheet("background-color:#199d89; color:#fff; font-weight:bold")
        self.ui.btn_cikar.setStyleSheet("background-color:#199d89; color:#fff; font-weight:bold ")
        self.ui.btn_carp.setStyleSheet("background-color:#199d89; color:#fff; font-weight:bold ")
        self.ui.btn_bol.setStyleSheet("background-color:#199d89; color:#fff; font-weight:bold ")
        

    def hesapla(self) : 
        sender = self.sender().text()
        if sender == "+" :
            self.ui.lbl_title.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())))
            self.ui.lbl_result.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text()))) 
            self.ui.lbl_result_2.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())))
            self.ui.sonuc.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())))
            print("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())))
        elif sender == "-" :
            self.ui.lbl_title.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())))
            self.ui.lbl_result.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text()))) 
            self.ui.lbl_result_2.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())))
            self.ui.sonuc.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())))
            print("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())))
        elif sender  == "x" :
            self.ui.lbl_title.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())))
            self.ui.lbl_result.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text()))) 
            self.ui.lbl_result_2.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())))
            self.ui.sonuc.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())))
            print("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())))
        elif sender  == "/" :
            self.ui.lbl_title.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())))
            self.ui.lbl_result.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())))
            self.ui.lbl_result_2.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())))
            self.ui.sonuc.setText("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())))
            print("Sonuç : "+ str(int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text()))) 


def app() :
    myapp = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(myapp.exec_()) 
    

app()


