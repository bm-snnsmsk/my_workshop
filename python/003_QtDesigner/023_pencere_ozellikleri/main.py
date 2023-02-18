from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import sys
from pencere import Ui_MainWindow

from PyQt5.QtCore import Qt ## pencerenin tüm dış çerçevesni kaldırmak için -- 111




class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint) ## pencerenin tüm dış çerçevesni kaldırmak için -- 222 ama görev çubuğundan kapatılabilir

       
    
        

       
        

        

    
        
    


        


    

  

      
        
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



        
            


    

        
       
        

        
    


        


    

