from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QTimer


from qtimer import Ui_MainWindow
from datetime import datetime




class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.timer=QTimer()
        self.timer.timeout.connect(self.show_time)
        

        self.ui.pushButton_start.clicked.connect(self.start_timer)
        self.ui.pushButton_stop.clicked.connect(self.stop_timer)

        self.show_time()
        

    def show_time(self) :
        tarih = datetime.now()
        self.ui.label.setText(str(tarih))

    def start_timer(self) :
        self.timer.start(1000)
        self.ui.pushButton_start.setEnabled(False)
        self.ui.pushButton_stop.setEnabled(True)

    def stop_timer(self) :
        self.timer.stop()
        self.ui.pushButton_start.setEnabled(True)
        self.ui.pushButton_stop.setEnabled(False)

  

    


     

       







    

        
       
        

        
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


