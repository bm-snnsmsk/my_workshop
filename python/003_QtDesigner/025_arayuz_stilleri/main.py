from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
import sys
from arayuz_stilleri import Ui_MainWindow





class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        print(QStyleFactory.keys()) ## mevcut stiller
        

      


       
        

        

    
        
    


        


    

  

      
        
def app() :
    app = QApplication(sys.argv)

    # app.setStyle("windowsvista")  ## varsayılan stil
    # app.setStyle("windows")
    app.setStyle("Fusion")

    win = Window()

    
    win.show()  
    sys.exit(app.exec_())  
    

app()



        
            


    

        
       
        

        
    


        


    

