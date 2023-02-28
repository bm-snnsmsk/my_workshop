from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtCore import QSize, Qt


import sys
from qpushbutton import Ui_MainWindow




class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_setText.setText("Durdur")
        self.ui.pushButton_setText.setWhatsThis("bu bir setWhatsThis örneğidir") # çalışması için bu butona odaklandıkatan sonra shift + F1 basılması lazıum

        self.ui.pushButton_icon.setIcon(QIcon(":/icons/start.ico"))
        self.ui.pushButton_icon.setIconSize(QSize(80, 80))

        self.ui.pushButton_icon_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.ui.pushButton_icon_2.setIcon(QIcon(":/icons/start.ico"))
        self.ui.pushButton_icon_2.setToolTip("F5 bas")
        self.ui.pushButton_icon_2.setShortcut("F5")
        self.ui.pushButton_icon_2.setShortcut(QKeySequence(Qt.CTRL+Qt.Key_P))
        self.ui.pushButton_icon_2.clicked.connect(self.tiklanma)



        self.ui.pushButton_icon_3.setCheckable(True)  ## clicked[bool] signalinin çalışabilmesi için  aksi takdirde sürekli False değeri döndürür
        self.ui.pushButton_icon_3.clicked[bool].connect(self.bool_slot) ## toggled[bool] = clicked[bool]
        self.ui.pushButton_icon_5.setCheckable(True) ## toggled[bool] signalinin çalışabilmesi için  aksi takdirde sürekli False değeri döndürür
        self.ui.pushButton_icon_5.toggled[bool].connect(self.bool_slot2) ## toggled[bool] = clicked[bool]


        self.ui.pushButton_icon_4.pressed.connect(self.pressed_slot)
        self.ui.pushButton_icon_4.released.connect(self.released_slot)



        self.ui.pushButton_icon_4.setText("")
        self.ui.pushButton_icon_4.setIcon(QIcon(":/icons/start.ico"))
    def pressed_slot(self) :
        self.ui.pushButton_icon_4.setIcon(QIcon(":/icons/stop.ico"))
        self.ui.pushButton_icon_4.setStyleSheet("background-color: rgba(255, 0, 0,0.7);")

    def released_slot(self) :
        self.ui.pushButton_icon_4.setIcon(QIcon(":/icons/start.ico"))
        self.ui.pushButton_icon_4.setStyleSheet("background-color: rgba(0, 255, 0,0.6);")



    def tiklanma(self) :
        print("f5'e basıldı")

    def bool_slot(self, val) :
        print("tuşlanma durumu : "+str(val))
        if val == True :
            self.ui.pushButton_icon_3.setText("Aç")
        else:
            self.ui.pushButton_icon_3.setText("Kapat")

    def bool_slot2(self, val) :
        print("tuşlanma durumu : "+str(val))
        if val == True :
            self.ui.pushButton_icon_5.setText("Aç")
        else:
            self.ui.pushButton_icon_5.setText("Kapat")



    def degistir(self, val) :
        if val == True :
            self.ui.pushButton_baslat.setText("Durdur")
            self.ui.pushButton_baslat.setStyleSheet("background-color: rgb(245, 0, 0);color: rgb(255, 255, 255);")
        else :
            self.ui.pushButton_baslat.setText("Başlat")
            self.ui.pushButton_baslat.setStyleSheet("background-color: rgb(0, 170, 0);color: rgb(255, 255, 255);")



    

        
       
        

        
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


