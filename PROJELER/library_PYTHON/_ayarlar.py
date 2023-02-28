from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

from ayarlar import Ui_Form
from data_base import DataBase





class Ayarlar(QWidget) :
    ayarlar_signal = pyqtSignal()
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
              
        self.db = DataBase('library.db')        
        self.ui.tableWidget.doubleClicked.connect(self.setAvailable)
        self.ui.lineEdit_search_books_settings.textChanged.connect(self.search_item)

    def setAvailable(self) :
        satir = self.ui.tableWidget.currentRow()
        id = self.ui.tableWidget.item(satir,0).text()
        kitap_adi = self.ui.tableWidget.item(satir,1).text()
        onay = QMessageBox.question(self, "Kütüphane Sistemi",f"{kitap_adi} isimli kitabı kiralanabilinir yapmak istediğinize emin mmisiniz ?", QMessageBox.Yes | QMessageBox.No)
        if onay == QMessageBox.Yes :
            is_update = self.db.updateData("UPDATE books SET booksState = ? WHERE booksID = ? ",[1, id])['data']
            print(is_update)
            if is_update == 1 :
                QMessageBox.information(self, "Kütüphane Sistemi",f"{kitap_adi} isimli kitap artık kiralanabilinir durumdadır.")
                self.load_books()
            else :
                QMessageBox.critical(self,"Kütüphane Sistemi","Güncellemede bir hata meydana geldi")
        else :
            QMessageBox.information(self,"Kütüphane Sistemi","Güncelleme işlemini iptal ettniz.")
            
    def load_books(self) :
        books = self.db.getDatas("SELECT * FROM books WHERE booksState = ? ORDER BY booksAddTime DESC",[0])['data']
        
        self.ui.tableWidget.setRowCount(len(books))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(("#ID","Kitap Adı","Yazar Adı","Yazar Soyadı","Durum"))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        counter = 0
        for i in books :
            self.ui.tableWidget.setItem(counter,0,QTableWidgetItem(str(i[0])))
            self.ui.tableWidget.setItem(counter,1,QTableWidgetItem(str(i[1])))
            self.ui.tableWidget.setItem(counter,2,QTableWidgetItem(str(i[2])))
            self.ui.tableWidget.setItem(counter,3,QTableWidgetItem(str(i[3])))
            self.ui.tableWidget.setItem(counter,4,QTableWidgetItem(str(i[9])))
            counter += 1
    
    ### search book START
    def search_item(self) :
        searched_item = self.ui.lineEdit_search_books_settings.text()
        
        result_search = self.db.getDatas("SELECT * FROM books WHERE booksState = ? AND (booksID LIKE '"+searched_item+"%' OR booksState LIKE '"+searched_item+"%' OR booksName LIKE '"+searched_item+"%' OR booksAuthorFirstName LIKE '"+searched_item+"%' OR booksAuthorLastName LIKE '"+searched_item+"%')", [0])['data']
        
        self.ui.tableWidget.setRowCount(len(result_search))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(("#ID","Kitap Adı", "Yazar Adı", "Yazar Soyadı", "Durum"))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        counter = 0
        for i in result_search :
            self.ui.tableWidget.setItem(counter,0,QTableWidgetItem(str(i[0])))
            self.ui.tableWidget.setItem(counter,1,QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(counter,2,QTableWidgetItem(i[2]))
            self.ui.tableWidget.setItem(counter,3,QTableWidgetItem(i[3]))
            self.ui.tableWidget.setItem(counter,4,QTableWidgetItem(str(i[9])))
            counter += 1
    ### search book END

        