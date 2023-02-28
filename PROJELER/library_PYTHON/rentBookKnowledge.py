from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from PyQt5.QtCore import pyqtSignal
from rent_book import Ui_MainWindow

from data_base import DataBase
from rent_book_kowledge import Ui_Dialog





class RentBookKnowledge(QDialog) :
    rent_book_signal = pyqtSignal(str, int)
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.label_bookID.setVisible(False)
        
        ### initial edits START
        self.dataBase = DataBase("library.db")
        ### initial edits END
        self.users()
        #self.ui.comboBox_uye_sec.currentIndexChanged.connect(self.select_user)
        self.ui.pushButton_rent_book.clicked.connect(self.rent_book_finish)

    def users(self) :
        users = self.dataBase.getDatas("SELECT * FROM users ORDER BY usersFirstName, usersLastName")['data']
        self.ui.comboBox_uye_sec.addItem("Üye Seç",0)
        for i in users :
            self.ui.comboBox_uye_sec.addItem(f"{i[1]} {i[2]}", i[0])
    
    def select_user(self) :
        print(self.ui.comboBox_uye_sec.currentData())
    
    def rent_book_finish(self) :
        bookID = self.ui.label_bookID.text()
        userID = self.ui.comboBox_uye_sec.currentData()
        self.rent_book_signal.emit(bookID, userID)
    
    def clear_rent_book_form(self) :
        self.ui.comboBox_uye_sec.setCurrentIndex(0)
        self.ui.label_bookID.setText("")
        self.ui.lineEdit_kitap_adi.setText("")
        self.ui.lineEdit_yazar_adi.setText("")



       