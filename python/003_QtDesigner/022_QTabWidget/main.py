from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from qtabwidget import Ui_MainWindow




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

        ## QtDesigner tarafından yapılsa bile burda bu şekilde belirtilmediği sürece tablar disenabled olmazlar
        self.ui.tabWidget.setTabEnabled(0,True)
        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.ui.tabWidget.setTabEnabled(3,False)
        self.ui.tabWidget.setTabEnabled(4,False)

        ## tab'daki x butonuyla ilgili tabı kapatmak için
        # ayrıca DİKKAT tabCloseRequested[int] şeklinde parametre istmiyor 
        self.ui.tabWidget.tabCloseRequested.connect(self.close_function)


        self.ui.pushButton.clicked.connect(self.login_slot)

        self.go_home_page() ## window her açıldığında anasayfa açılması için

        

        

    # --------------------------------
    def login_slot(self) :
        name = self.ui.lineEdit_kullanici_adi.text() 
        parola = self.ui.lineEdit_parola.text()

       
        if name == "admin" and parola == "111" :
            self.ui.statusbar.showMessage("Giriş başarılı",self.statusbar_time)
            self.ui.tabWidget.setCurrentIndex(1) 
            self.ui.tabWidget.setTabEnabled(0,True)
            self.ui.tabWidget.setTabEnabled(1,True)
            self.ui.tabWidget.setTabEnabled(2,True)
            self.ui.tabWidget.setTabEnabled(3,True)
            self.ui.tabWidget.setTabEnabled(4,True)
            self.ui.lineEdit_kullanici_adi.clear() 
            self.ui.lineEdit_parola.clear()
        else :
            self.ui.statusbar.showMessage("Kullanıcı Adı veya şifre hatalı",self.statusbar_time)
            QMessageBox.warning(self,"Hatalı Giriş","Kullanıcı adı veya şifre hatalı")
            self.ui.lineEdit_kullanici_adi.clear() 
            self.ui.lineEdit_parola.clear() 
       

    # --------------------------------
    def go_home_page(self) :
        self.ui.tabWidget.setCurrentIndex(self.home_page_index) 
        # self.ui.tabWidget.setTabEnabled(0,True)
        # self.ui.tabWidget.setTabEnabled(1,False)
        # self.ui.tabWidget.setTabEnabled(2,False)
        # self.ui.tabWidget.setTabEnabled(3,False)
        # self.ui.tabWidget.setTabEnabled(4,False)
        self.ui.statusbar.showMessage("go home",2000)

  
  

    ### --------------------------------------------------
    def close_function(self, index) :
        print(index)
        if index != 0 :
            self.ui.tabWidget.removeTab(index)

    
        

       
        

        

    
        
    


        


    

  

      
        
def app() :
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()



        
            


    

        
       
        

        
    


        


    

