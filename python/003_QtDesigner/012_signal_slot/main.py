from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
import sys
from untitled import Ui_MainWindow

## 333 - signal (decoratif fonksiyon için) 
from PyQt5.QtCore import pyqtSlot 

## 444 - signal (decoratif fonksiyon için) 
from PyQt5.QtCore import pyqtSignal



class Window(QtWidgets.QMainWindow):

    ## 444 ve 555 örnekleri için signal tanımlama
    my_signal = pyqtSignal(int)  ## parametre almıyorsa boş bırakılır
    ###############################

    def __init__(self):

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    ### 111  QtDesigner da signal tanımlandıktan ve edit kısmından my_slot isimli slot tanımlandıktan sonra hazırladığımız slotun içeriği
    # def my_slot(self, deg) :
    #     self.ui.label_ekran.setText(str(deg))


    ## 222 - signal
        #self.ui.horizontalSlider.valueChanged[int].connect(self.my_slot)
    ## 222 - slot
    # def my_slot(self, val) :
    #     self.ui.label_ekran.setText("değer : "+str(val))

    ## 333 - slot
    # @pyqtSlot(int) ## parametre almıyorsa boş bırakılır
    # def on_horizontalSlider_valueChanged(self, val) : ## isimlendirme bu formatta olmalı
    #     self.ui.label_ekran.setStyleSheet("font-size:16px")
    #     self.ui.label_ekran.setText("@pyqtSlot - değer : "+str(val))

    ## 444 (kulağı tersten tutmaktır) (signal-signal-slot)
    #     self.ui.horizontalSlider.valueChanged[int].connect(self.my_signal[int])
    #     self.my_signal[int].connect(self.my_slot)
    # def my_slot(self, val) :
    #     self.ui.label_ekran.setText("değer : "+str(val))


    ## 555 emit() (signal-slot-emit()-signal-slot)
        self.ui.horizontalSlider.valueChanged[int].connect(self.kaydirici_slot)
        self.my_signal[int].connect(self.my_slot)
    def kaydirici_slot(self, val) :
        if val == 50 :            
            self.ui.horizontalSlider.valueChanged[int].disconnect(self.kaydirici_slot)            
        self.my_signal.emit(val)
    def my_slot(self, val) :
         self.ui.label_ekran.setText("emit(val) değer : "+str(val))



    

    


    



  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


