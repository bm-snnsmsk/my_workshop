from PyQt5 import QtWidgets
import sys
from qdatetime import Ui_MainWindow

from datetime import datetime




class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.dateEdit.dateChanged.connect(self.date_function)  ## enter'a basıldıktan sonra çalışan signal
        self.ui.dateEdit.editingFinished.connect(self.date_function2) ## enter'a basıldıktan sonra çalışan signal


        self.ui.timeEdit.timeChanged.connect(self.time_function)
        self.ui.timeEdit.editingFinished.connect(self.time_function2) ## enter'a basıldıktan sonra çalışan signal

        self.ui.dateTimeEdit.timeChanged.connect(self.dateTime_function)
        self.ui.dateTimeEdit.editingFinished.connect(self.dateTime_function2) ## enter'a basıldıktan sonra çalışan signal

        

        self.simdi()

    ## --------------------------------------------------------------------------------------------
    def date_function(self) :
        date = self.ui.dateEdit.date() 
        self.ui.label.setText(str(date.day()))
        self.ui.label_2.setText(str(date.month()))
        self.ui.label_3.setText(str(date.year()))
       

    def date_function2(self) :
        date = self.ui.dateEdit.date() 
        self.ui.label.setText(str(date.day()))
        self.ui.label_2.setText(str(date.month()))
        self.ui.label_3.setText(str(date.year()))
    #---------------------------------------------------------------------


    
    ## ---------------------------------------------------------------   
    def time_function(self) :
        time = self.ui.timeEdit.time() 
        self.ui.label.setText(str(time.hour()))
        self.ui.label_2.setText(str(time.minute()))
        self.ui.label_3.setText(str(time.second()))

    def time_function2(self) :
        time = self.ui.timeEdit.time() 
        self.ui.label.setText(str(time.hour()))
        self.ui.label_2.setText(str(time.minute()))
        self.ui.label_3.setText(str(time.second()))


    ## -------------------------------------------------------------

    def dateTime_function(self) :
        date = self.ui.dateTimeEdit.date() 
        time = self.ui.dateTimeEdit.time() 
        self.ui.label.setText(str(date.day()))
        self.ui.label_2.setText(str(date.month()))
        self.ui.label_3.setText(str(date.year()))
        self.ui.label_4.setText(str(time.hour()))
        self.ui.label_5.setText(str(time.minute()))       


    def dateTime_function2(self) :
        date = self.ui.dateTimeEdit.date() 
        time = self.ui.dateTimeEdit.time() 
        self.ui.label.setText(str(date.day()))
        self.ui.label_2.setText(str(date.month()))
        self.ui.label_3.setText(str(date.year()))
        self.ui.label_4.setText(str(time.hour()))
        self.ui.label_5.setText(str(time.minute()))

    def simdi(self) :
        self.simdi = datetime.now()
        self.yil = datetime.now().year
        self.ay = datetime.now().month
        self.gun = datetime.now().day
        self.saat = datetime.now().hour
        self.dakika = datetime.now().minute
        self.saniye = datetime.now().second

        self.ui.label.setText(str(self.gun))
        self.ui.label_2.setText(str(self.ay))
        self.ui.label_3.setText(str(self.yil))
        self.ui.label_4.setText(str(self.saat))
        self.ui.label_5.setText(str(self.dakika))
        self.ui.label_6.setText(str(self.saniye))

       







    

        
       
        

        
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


