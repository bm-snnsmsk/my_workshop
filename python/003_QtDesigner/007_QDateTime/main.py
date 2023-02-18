from PyQt5 import QtWidgets
import sys
from datetimeedit import Ui_MainWindow

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
        ##############  tarih zaman fonksiyonlar START ###############
        print("-------------------------------------------------")
        now = QDate.currentDate()  
        print(now.toString(Qt.ISODate))  ## 2022-11-28
        print(now.toString(Qt.DefaultLocaleLongDate)) ## 28 Kasım 2022 Pazartesi

        datetime = QDateTime.currentDateTime()
        print(datetime.toString())  ## Pzt Kas 28 21:13:37 2022

        time = QTime.currentTime()
        print(time.toString(Qt.DefaultLocaleLongDate))  ## 21:13:37
        print("-------------------------------------------------")
        ##############  tarih zaman fonksiyonlar END ###############

        self.ui.btn_tarih.clicked.connect(self.calculate)

    def calculate(self) :
        now = QDate.currentDate()
        start = self.ui.d_edit_start.date()
        end = self.ui.d_edit_end.date()
        zaman = self.ui.t_edit.time()
        date_time = self.ui.dt_edit.date()
        
        print(start, end)
        print("days in month : {0}".format(start.daysInMonth()))
        print("days in year : {0}".format(start.daysInYear()))
        print("toplam days : {0}".format(start.daysTo(end))) ## end ile start tarihleri arasında kaç gün var
        print("toplam days : {0}".format(start.daysTo(now))) ## start ile şimdi tarihleri arasında kaç gün var
        print("zaman : {0}".format(zaman)) 
        print("zaman saat: {0}".format(zaman.hour())) 
        print("zaman dakika: {0}".format(zaman.minute())) 
        print("zaman saniye: {0}".format(zaman.second())) 
        print("ileri tarih : {0}".format(now.addDays(12))) 
        print("ileri tarih gün: {0}".format(now.addDays(12).day())) 
        print("ileri tarih ay: {0}".format(now.addDays(12).month())) 
        print("ileri tarih yıl: {0}".format(now.addDays(12).year())) 
        print("ileri tarih : {0}".format(now.addMonths(12))) 
        print("ileri tarih : {0}".format(now.addYears(12))) 
        print("date time day(): {0}".format(date_time.day())) 
        print("date time month(): {0}".format(date_time.month())) 
        print("date time year(): {0}".format(date_time.year())) 
        print(date_time.toString())


      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


