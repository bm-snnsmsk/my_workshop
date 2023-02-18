from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from qstackedwidget import Ui_MainWindow
import random
from PyQt5.QtGui import QIntValidator


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.home_page_index = 0
        self.kitaplar_page_index = 1
        self.kitap_ekle_page_index = 2
        self.kullanicilar_page_index = 3
        self.kullanici_ekle_page_index = 4

        self.statusbar_time = 2500

        self.ui.lineEdit_result.setValidator(QIntValidator(0,200,self)) ##☺ kullanıcı bu aralıkta ve sadece sayı girebilsin diye

        self.ui.actionAnasayfa.triggered.connect(self.go_home_page)
        self.ui.actionKitaplar.triggered.connect(self.go_kitaplar_page)
        self.ui.actionKitap_Ekle.triggered.connect(self.go_kitap_ekle_page)
        self.ui.actionUyeler.triggered.connect(self.go_uyeler_page)
        self.ui.actionUyeEkle.triggered.connect(self.go_uye_ekle_page)

        self.ui.pushButton.clicked.connect(self.login_slot)

        self.go_home_page() ## window her açıldığında anasayfa açılması için

        

        

    # --------------------------------
    def login_slot(self) :
        name = self.ui.lineEdit_kullanici_adi.text() 
        parola = self.ui.lineEdit_parola.text()

        result = self.sayi1 + self.sayi2

      

        if self.ui.lineEdit_result.text() != "" or len(self.ui.lineEdit_result.text()) != 0 :
            if name == "admin" and parola == "111" and result == int(self.ui.lineEdit_result.text()):
                self.ui.statusbar.showMessage("Giriş başarılı",self.statusbar_time)
                self.ui.toolBar.setEnabled(True)
                self.ui.menubar.setEnabled(True)
                self.go_kitaplar_page()
                self.ui.lineEdit_kullanici_adi.clear() 
                self.ui.lineEdit_parola.clear() 
                self.ui.lineEdit_result.clear() 
            else :
                self.ui.statusbar.showMessage("Kullanıcı Adı veya şifre hatalı",self.statusbar_time)
                QMessageBox.warning(self,"Hatalı Giriş","Kullanıcı adı veya şifre hatalı")
                self.ui.lineEdit_kullanici_adi.clear() 
                self.ui.lineEdit_parola.clear() 
                self.ui.lineEdit_result.clear() 
        else :
            QMessageBox.warning(self,"İşlem","işlemi boş bırakmamalısnız")

    # --------------------------------
    def go_home_page(self) :

        self.sayi1 = random.randint(0, 100)
        self.sayi2 = random.randint(0, 100)
        self.ui.lineEdit_result.clear()
        self.ui.label_sayi1.setText(str(self.sayi1))
        self.ui.label_sayi2.setText(str(self.sayi2))

        self.ui.stackedWidget.setCurrentIndex(self.home_page_index) 
        self.ui.toolBar.setEnabled(False)
        self.ui.menubar.setEnabled(False)

    # --------------------------------
    def go_kitaplar_page(self) :
        self.ui.stackedWidget.setCurrentIndex(self.kitaplar_page_index)  

    # --------------------------------
    def go_kitap_ekle_page(self) :
        self.ui.stackedWidget.setCurrentIndex(self.kitap_ekle_page_index)  

    # --------------------------------
    def go_uyeler_page(self) :
        self.ui.stackedWidget.setCurrentIndex(self.kullanicilar_page_index)  
    
    # --------------------------------
    def go_uye_ekle_page(self) :
        self.ui.stackedWidget.setCurrentIndex(self.kullanici_ekle_page_index)  

    
    
        
    


        


    

  

      
        
def app() :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()



        
            


    

        
       
        

        
    


        


    

