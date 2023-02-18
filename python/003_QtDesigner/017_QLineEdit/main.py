from PyQt5 import QtWidgets
import sys
from qlineedit import Ui_MainWindow


## QLineEdit'e sadece int değer girmesini zorlama
from PyQt5.QtGui import QIntValidator



class Window(QtWidgets.QMainWindow):
    show_duration = 1500
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit_deger_yazma.setEnabled(False)
        self.ui.lineEdit_signal_slot.returnPressed.connect(self.my_slot) ## bu fonksiyon, QLineEdit'e bir şeyler yazılıp ENTER'a basılınca çalışır
        self.ui.lineEdit_deger_okuma.returnPressed.connect(self.my_slot2) 

        ## QLineEdit'i kısıtlamak
        self.ui.lineEdit_tamsayi.setValidator(QIntValidator(0,200,self))

        ## sadece okunabilir
        self.ui.lineEdit_okunabilir.setReadOnly(True)

        ## password
        ## self.ui.lineEdit_sifre.setEchoMode(2)  ## veya 
        self.ui.lineEdit_sifre.setEchoMode(QtWidgets.QLineEdit.Password)

        ## placeholder
        self.ui.lineEdit_placeholder.setPlaceholderText("placeholder ipucu")

        ## tooltip
        self.ui.lineEdit_aciklayici.setToolTip("bu input tooltip örneğidir")

        ## içerik sürükleme
        self.ui.lineEdit_surukleme.setDragEnabled(True)

        ## maxlength
        self.ui.lineEdit_icerik_uzunlugu.setMaxLength(11)

        ## içerik temizleme
        self.ui.lineEdit_icerik_temizleme.clear()


    def my_slot(self) :
        print(self.ui.lineEdit_signal_slot.text())
        

    def my_slot2(self) :
        txt1 = self.ui.lineEdit_signal_slot.text()
        txt2 = self.ui.lineEdit_deger_okuma.text()
        self.ui.lineEdit_deger_yazma.setText(txt1 + " - "+txt2)
         ## içerik temizleme
        self.ui.lineEdit_signal_slot.clear()
        self.ui.lineEdit_deger_okuma.clear()

        
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


