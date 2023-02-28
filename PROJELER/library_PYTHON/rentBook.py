from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

from rent_book import Ui_MainWindow
from datetime import datetime
from datetime import timedelta
from data_base import DataBase
from rentBookKnowledge import RentBookKnowledge





class RentBook(QMainWindow) :
    
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ### initial edits START
        self.setWindowTitle("Kütüphane Sistemi")
        self.dataBase = DataBase("library.db")        
        ### initial edits END

        self.rentBookKnowledge = RentBookKnowledge()
        self.rentBookKnowledge.rent_book_signal.connect(self.rent_book_last_step)

        self.ui.lineEdit.textChanged.connect(self.search_book)
        self.ui.tableWidget.doubleClicked.connect(self.rent_book)
        ##self.get_book_list()
        self.isRentAble()
    
    def get_book_list(self) :
        books = self.dataBase.getDatas('SELECT * FROM books WHERE booksState = ? ORDER BY booksAddTime DESC', [1])['data']          
        
        self.ui.tableWidget.setRowCount(len(books))
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setHorizontalHeaderLabels(("ID","Kitap Adı", "Yazar Adı", "Yazar Soyadı"))
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 350)
        self.ui.tableWidget.setColumnWidth(2, 250)
        self.ui.tableWidget.setColumnWidth(3, 250)
        
        for indexsatir, kayit in enumerate(books) :
            for indexsutun, kayitsutun in enumerate(kayit) :
                self.ui.tableWidget.setItem(indexsatir,indexsutun,QTableWidgetItem(str(kayitsutun)))
      
    def search_book(self) :
        searched_item = self.ui.lineEdit.text()
        
        result_search = self.dataBase.getDatas("SELECT * FROM books WHERE booksState = ? AND (booksID LIKE '"+searched_item+"%' OR booksName LIKE '"+searched_item+"%' OR booksAuthorFirstName LIKE '"+searched_item+"%' OR booksAuthorLastName LIKE '"+searched_item+"%')", [1])['data']
        
        self.ui.tableWidget.setRowCount(len(result_search))
        self.ui.tableWidget.setColumnCount(5)
        self.ui.tableWidget.setHorizontalHeaderLabels(("#ID","Kitap Adı", "Yazar Adı", "Yazar Soyadı", "Kirala"))
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 250)
        self.ui.tableWidget.setColumnWidth(2, 250)
        self.ui.tableWidget.setColumnWidth(3, 120)
        self.ui.tableWidget.setColumnWidth(4, 110)

        counter = 0
        for i in result_search :
            self.ui.tableWidget.setItem(counter,0,QTableWidgetItem(str(i[0])))
            self.ui.tableWidget.setItem(counter,1,QTableWidgetItem(i[1]))
            self.ui.tableWidget.setItem(counter,2,QTableWidgetItem(i[2]))
            self.ui.tableWidget.setItem(counter,3,QTableWidgetItem(i[3]))
            self.ui.tableWidget.setItem(counter,4,QTableWidgetItem("Kirala"))
            counter += 1

    def rent_book(self) :
        selected_item = self.ui.tableWidget.currentRow()
        selected_id = self.ui.tableWidget.item(selected_item,0).text()
        selected_book_name = self.ui.tableWidget.item(selected_item,1).text()
        selected_author_first_name = self.ui.tableWidget.item(selected_item,2).text()
        selected_author_last_name = self.ui.tableWidget.item(selected_item,3).text()
        self.rentBookKnowledge.ui.label_bookID.setText(selected_id)
        self.rentBookKnowledge.ui.lineEdit_kitap_adi.setText(selected_book_name)
        self.rentBookKnowledge.ui.lineEdit_yazar_adi.setText(f"{selected_author_first_name} {selected_author_last_name}")
        self.rentBookKnowledge.show()
      
    def rent_book_last_step(self, bookID, userID) :   
        if userID == 0 :
            QMessageBox.critical(self.rentBookKnowledge, "Kütüphane Sistemi", "Lütfen bir üye seçiniz.")     
        else :
            sql = "UPDATE books SET booksState = ? WHERE booksID = ?"
            self.dataBase.updateData(sql, [0, bookID])
            sql2 = "INSERT INTO rent (rentBookID, rentUserID, rentDate, rentBringItBackDate) VALUES (?, ?, ?, ?)"
            self.dataBase.insertData(sql2, [bookID, userID, datetime.now(), (datetime.timestamp(datetime.now() + timedelta(days = 15)))])
            # print(bookID)
            # print(userID)
            if sql and sql2 :
                QMessageBox.information(self,"Kütüphane sistemi","işlem başarılı")
                self.rentBookKnowledge.clear_rent_book_form()
                self.get_book_list()
                self.rentBookKnowledge.close()
                self.close()
            else :
                QMessageBox.critical(self,"Kütüphane sistemi","işlem başarısız")
    
    def isRentAble(self) :
        sql = "select b.booksID, r.rentBringItBackDate from books as b inner join rent as r on b.booksID = r.rentBookID WHERE rentState = ?"
        availableBooks = self.dataBase.getDatas(sql, [1])['data']
        for i in availableBooks :
            # print(type(i[1]))
            # print(i)            
            # print(str(i[0])+ " --- "+str(i[1]))
            if datetime.timestamp(datetime.now()) > i[1] :
                sql = "UPDATE books SET booksState = ? WHERE booksID = ?"
                self.dataBase.updateData(sql, [1, i[0]])
        self.get_book_list()
           

    