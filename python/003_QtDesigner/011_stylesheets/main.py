from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from untitled import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.setStyleSheet("color:red")


        ### qtdesignerdan stylesheet tanımlanırken, widget'lerin obje adları 
        ### id olarak kullanılır css'de olduğu gibi
        ### ayrıca layotlara stylesheet tanımlamak için öncelikle sağ-click ile morph-into  seçeneği ile QWidget veya QFrame çevirerek bu widgetlerin özelikleri inherit yapılır
        ### #cetralwidget {border-image:url(:/icons/arkaplan_image.png)}
        
        
  

      
   



   
   
    

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


