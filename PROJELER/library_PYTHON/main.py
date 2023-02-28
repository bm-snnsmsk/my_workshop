from PyQt5.QtWidgets import *
import sys

from login import Ui_Form
from homePage import HomePage





class MainWindow(QWidget) : 
      
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form() ## giriş Penceresi yapılması istenen form/window
        self.ui.setupUi(self)

        self.ui.pushButton_login.clicked.connect(self.login_to_library)
        self.ui.lineEdit_login_parola.setEchoMode(QLineEdit.Password)
        self.homePage = HomePage()
        
       

    
    def login_to_library(self) :
        admin_table = self.homePage.dataBase.getData("SELECT * FROM admin")['data']       
         
        email_name = self.ui.lineEdit_login_email.text()
        password = self.ui.lineEdit_login_parola.text()
        if not email_name :
            QMessageBox.critical(self, "Kütüphane Sistemi", "<h1 style='color:red'>Lütfen email alanını boş bırakmayınız! <a href='google.com'>tıkla</a> </h1>")
        elif not password :
            QMessageBox.critical(self, "Kütüphane Sistemi", "Lütfen parola alanını boş bırakmayınız!")
        elif not email_name == admin_table[3] or not password == admin_table[4] :
            QMessageBox.critical(self, "Kütüphane Sistemi", "Email adresiniz veya parolanız yanlış!")
        else :           
            QMessageBox.information(self, "Kütüphane Sistemi", "Kütüphane Sistemine Hoş Geldiniz !")                       
            self.homePage.show()
            self.homePage.ui.statusbar.showMessage("Kütüphane Sitemi'ne giriş yapıldı...",2000)
            self.close()


def app() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()

        











      






        



