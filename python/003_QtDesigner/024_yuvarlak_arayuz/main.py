from PyQt5.QtWidgets import QMainWindow, QApplication ,qApp
import sys
from yuvarlak_arayuz import Ui_MainWindow

## 1. yöntem
from PyQt5.QtGui import QRegion, QIcon

## 2. yöntem
from PyQt5.QtCore import QRect






class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

      

       
        ## 1. yöntem // full_screen_function() fonksiyonu düzgün çalışmadığı için böyle bir fonksiyona eklendi
        self.update_and_mask()
    
        
        ## 2. yöntem

        # sekil2 = QRect(0,0,self.width(), self.height())
        # result = QRegion(sekil2, QRegion.Ellipse)
        # self.setMask(result)

        self.ui.pushButton_close.clicked.connect(self.close_function)
        self.ui.pushButton_full_screen.clicked.connect(self.full_screen_function)
        self.ui.pushButton_minimize.clicked.connect(self.minimize_function)

    def close_function(self):
        self.close()

    def full_screen_function(self):
        ## iki durumlu yapmak için
        if self.isMaximized() :
            self.showNormal()
            self.ui.pushButton_full_screen.setIcon(QIcon(":/img/maximize.ico"))
        else :
            self.showMaximized()
            self.ui.pushButton_full_screen.setIcon(QIcon(":/img/minimize.ico"))

        ## 1. yöntem // full_screen_function() fonksiyonu düzgün çalışmadığı için böyle bir fonksiyona eklendi
        self.update_and_mask()

    def minimize_function(self):
        self.showMinimized()
    
    def update_and_mask(self) :
        qApp.processEvents() ## kendini güncelle sonra maskeleme yap
        ## 1. yöntem // full_screen_function() fonksiyonu düzgün çalışmadığı için böyle bir fonksiyona eklendi
        sekil = QRegion(self.rect(), QRegion.Ellipse)
        self.setMask(sekil)

    
        

       
        

        

    
        
    


        


    

  

      
        
def app() :
    app = QApplication(sys.argv)
    win = Window()

    ## -------------------------------------------------------------
    win.show()  ## belirlenmiş pencere ölçülerinde açılır
    # win.showMinimized() ## ilk açıldığında gözükmez ama görev çubuğundan çağrıldığında belirlenmiş ölçülerde açılır 
    # win.showMaximized() ## maximum pencere ölçülerinde açılır
    # win.showFullScreen() ## maximum pencere ölçülerinde açılır  ## alt+tab tuşuyla bu fullekrandan çıkılabilir

    sys.exit(app.exec_())  
    

app()



        
            


    

        
       
        

        
    


        


    

