from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import sys

from datetime import datetime


from data_base import DataBase
from home_page import Ui_MainWindow
from addBook import AddBook
from addUser import AddUser
from rentBook import RentBook
from _ayarlar import Ayarlar



class HomePage(QMainWindow) :
    
    def __init__(self) :
        super(HomePage, self).__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
     
                
        ### init definitions and functions START
        self.setWindowTitle("Kütüphane Otomasyonu")        
        self.dataBase = DataBase("library.db")
        self.load_book_list()
        ### init definitions and functions END        

        ### time definitions START
        self.timer = QTimer()
        self.show_current_time()
        self.timer.timeout.connect(self.show_current_time)        
        ### time definitions END

        ### add book sayfasına yönlendirme START
        self.addBook = AddBook()   
        self.ui.pushButton_add_book.clicked.connect(self.open_add_new_book_page)
        self.addBook.add_book_signal.connect(self.add_new_book_knowledges)
        ### add book sayfasına yönlendirme END

        ### refresh START
        self.ui.pushButton_refresh_books_list.clicked.connect(self.refresh_book_list)        
        ### refresh END

        ### add new user START
        self.addUser = AddUser()   
        self.ui.pushButton_add_user.clicked.connect(self.open_add_new_user_page)
        self.addUser.add_user_signal.connect(self.add_new_user_knowledges)
        ###  add new user END

        ### list users START
        self.ui.pushButton_list_users.clicked.connect(self.list_users)
        ### list users END

        ### search item START
        self.ui.lineEdit_search.textChanged.connect(self.search_item)
        ### search item END

        ## logout START
        self.ui.pushButton_logout.clicked.connect(self.logout) 
        ## logout END

        ## rent book START
        self.rentBook = RentBook() 
        self.ui.pushButton_rent_book.clicked.connect(self.open_rent_book_page) 
        #self.rentBook.rent_book_signal.connect(self.rent_book_knowledges)
        ## rent book END

        ## ayarlar START
        self.ayarlar = Ayarlar()
        self.ui.pushButton_settings.clicked.connect(self.go_ayarlar_page)
        ## ayarlar END

        ## kayıt sil START
        self.ui.tableWidget_list_books.doubleClicked.connect(self.delete_row)
        ## kayıt sil END
              
    ## kayıt silme fonksiyon START   
    def delete_row(self) :
        satir = self.ui.tableWidget_list_books.currentRow()
        bookID = self.ui.tableWidget_list_books.item(satir, 0).text()
        bookName = self.ui.tableWidget_list_books.item(satir, 1).text()
        onay = QMessageBox.question(self,"Kütüphane Sisemi",f"{bookName} isimli kayıt Kayıt silinecektir. Devam etmek istiyor musunuz ?", QMessageBox.Yes | QMessageBox.No)
        if onay == QMessageBox.Yes :
            is_del = self.dataBase.deleteData("DELETE FROM books WHERE booksID = ?", [bookID])["data"]
            if is_del == 1 :
                QMessageBox.information(self,"Kütüphane Sistemi","Kaydınız başarılı bir şekilde silinmiştir")
                self.dataBase.updateData("update rent set rentState = ? WHERE rentBookID = ?", [0, bookID])
                self.load_book_list()
            else :
                QMessageBox.critical(self,"Kütüphane Sistemi","Kaydınız silinemedi")
        else :
            QMessageBox.critical(self,"Kütüphane Sistemi","Kayıt silme işlemi iptal edilmiştir.")
    ## kayıt silme fonksiyon END 

    def go_ayarlar_page(self) :
        self.ayarlar.load_books()
        self.ayarlar.show()

    def logout(self) :
        logout = QMessageBox.question(self,"Kütüphane Sistemi", "Kütüphane Sistem'nden çıkış yapmak üzeresiniz. Devam etmek istiyor musunuz ?", QMessageBox.Yes, QMessageBox.No)
        if logout == QMessageBox.Yes :
            self.ui.statusbar.showMessage("Kütüphane Sitemi'nden çıkılıyor...",2000)
            # self.close()            
            sys.exit()
        ###  logout END    
            
    def load_book_list(self) :        
        books = self.dataBase.getDatas('SELECT * FROM books ORDER BY booksAddTime DESC')['data']     
        
        self.ui.tableWidget_list_books.setRowCount(len(books))
        self.ui.tableWidget_list_books.setColumnCount(5)
        self.ui.tableWidget_list_books.setHorizontalHeaderLabels(("#ID","Kitap Adı", "Yazar Adı", "Yazar Soyadı", "Durum"))
        self.ui.tableWidget_list_books.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        counter = 0
        for i in books :
            self.ui.tableWidget_list_books.setItem(counter,0,QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_list_books.setItem(counter,1,QTableWidgetItem(i[1]))
            self.ui.tableWidget_list_books.setItem(counter,2,QTableWidgetItem(i[2]))
            self.ui.tableWidget_list_books.setItem(counter,3,QTableWidgetItem(i[3]))
            self.ui.tableWidget_list_books.setItem(counter,4,QTableWidgetItem(str(i[9])))
            counter += 1
    
    def refresh_book_list(self) :
        self.ui.statusbar.showMessage("Kütüphane Sitemi listesi yenilendi...",2000)
        self.load_book_list()

    ### list users START
    def list_users(self) :
        self.ui.statusbar.showMessage("Kullanıcılar listelendi... ",2000)
          
        users = self.dataBase.getDatas('SELECT * FROM users ORDER BY usersFirstName, usersLastName DESC')['data'] 
        
        self.ui.tableWidget_list_books.setRowCount(len(users))
        self.ui.tableWidget_list_books.setColumnCount(5)
        self.ui.tableWidget_list_books.setHorizontalHeaderLabels(("Adı", "Soyadı", "Email", "Telefon","Detay"))
      
        self.ui.tableWidget_list_books.setColumnWidth(0, 200)
        self.ui.tableWidget_list_books.setColumnWidth(1, 200)
        self.ui.tableWidget_list_books.setColumnWidth(2, 200)
        self.ui.tableWidget_list_books.setColumnWidth(3, 200)
        self.ui.tableWidget_list_books.setColumnWidth(4, 150)         

        counter = 0
        for i in users :
            self.ui.tableWidget_list_books.setItem(counter,0,QTableWidgetItem(i[1]))
            self.ui.tableWidget_list_books.setItem(counter,1,QTableWidgetItem(i[2]))
            self.ui.tableWidget_list_books.setItem(counter,2,QTableWidgetItem(i[3]))
            self.ui.tableWidget_list_books.setItem(counter,3,QTableWidgetItem(i[4]))
            self.ui.tableWidget_list_books.setItem(counter,4,QTableWidgetItem("detaya git"))
            counter += 1
    ### list users END         
 
    ### time functions START
    def show_current_time(self) :
        self.timer.start(1000)        
        current_year = str(datetime.now().year)
        current_month = str(datetime.now().month)
        current_day = str(datetime.now().day)
        current_hour = str(datetime.now().hour)
        current_minute = str(datetime.now().minute)
        current_second = str(datetime.now().second)
        if len(current_month) == 1 :
            current_month = "0"+ current_month
        if len(current_day) == 1 :
            current_day = "0"+ current_day
        if len(current_hour) == 1 :
            current_hour = "0"+ current_hour
        if len(current_minute) == 1 :
            current_minute = "0"+ current_minute
        if len(current_second) == 1 :
            current_second = "0"+ current_second
        self.ui.label_date.setText(current_day+"."+current_month+"."+current_year+" "+current_hour+"."+current_minute+"."+current_second)
    ### time functions END

    ### add book sayfasına yönlendirme functions START
    def open_add_new_book_page(self) :
        # self.addBook.ui.label_add_book_form_title.setText("deneme : "+self.ui.pushButton_add_book.text())  ### karşı forma bilgi gönderme ÖRNEK KOD SATIRI
        self.addBook.show()
        self.close()

    def add_new_book_knowledges(self, book_name, author_first_name, author_last_name, category, publisher, page_count, language, description) :
        if not book_name or not author_first_name or not author_last_name or not category or not publisher or not page_count or not language or not description:
            QMessageBox.critical(self, "Kütüphane Sistemi", "Lütfen Boş alan bırakmayınız! ")
        else : 
            sql = "INSERT INTO books (booksName, booksAuthorFirstName, booksAuthorLastName, booksCategory, booksPublisher, booksPageCount, booksLanguage, booksDescription, booksState, booksAddTime) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"            
            values = (book_name, author_first_name, author_last_name, category,  publisher, page_count, language, description, "1", str(datetime.now()))
            isInsert = self.dataBase.insertData(sql, values=values)
            
            if isInsert['data'] :
                QMessageBox.information(self, "Kütüphane Sistemi", f"{isInsert['data']} tane kayıt eklendi")  
                self.ui.statusbar.showMessage(f"{isInsert['data']} tane kayıt eklendi",2000)
                self.load_book_list() 
                self.rentBook.get_book_list() 
                self.addBook.clear_add_book_form()             
                self.addBook.close()
                self.show()
            else : 
                QMessageBox.critical(self, "Kütüphane Sistemi", "Kayıt ekleme sırasında bir hata meydana geldi")             
    ### add book sayfasına yönlendirme functions END

    ### open add new user functions START
    def open_add_new_user_page(self) :
        self.addUser.show()
    ### open add new user functions END

    def add_new_user_knowledges(self, user_first_name, user_last_name, user_email, user_phone_number, user_photo) :        
        if not user_first_name or not user_last_name or not user_email or not user_phone_number :
            QMessageBox.critical(self, "Kütüphane Sistemi", "Lütfen boş alan bırakmayınız !")         
        else :
            if not user_photo :
                user_photo = "erkek_avatar.png"
            sql = "INSERT INTO users (usersFirstName, usersLastName, usersEmail, usersPhoneNumber, usersProfileImage, usersState, usersAddTime) VALUES(?, ?, ?, ?, ?, ?, ?)"            
            values = (user_first_name, user_last_name, user_email, user_phone_number, user_photo, "1", str(datetime.now()))
            isInsert = self.dataBase.insertData(sql, values=values)
            
            if isInsert['data'] :
                QMessageBox.information(self, "Kütüphane Sistemi", f"{isInsert['data']} tane kullanıcı eklendi") 
                self.list_users()
                self.ui.statusbar.showMessage(f"{isInsert['data']} tane kullanıcı eklendi", 2000)
                self.addUser.clear_add_user_form()           
                self.addUser.close()
                self.show()
            else : 
                QMessageBox.critical(self, "Kütüphane Sistemi", "Kayıt ekleme sırasında bir hata meydana geldi") 
    ###  add new user functions END

    ### search book START
    def search_item(self) :
        searched_item = self.ui.lineEdit_search.text()
        
        result_search = self.dataBase.getDatas("SELECT * FROM books WHERE booksState LIKE '"+searched_item+"%' OR booksName LIKE '"+searched_item+"%' OR booksAuthorFirstName LIKE '"+searched_item+"%' OR booksAuthorLastName LIKE '"+searched_item+"%' ")['data']
        
        self.ui.tableWidget_list_books.setRowCount(len(result_search))
        self.ui.tableWidget_list_books.setColumnCount(5)
        self.ui.tableWidget_list_books.setHorizontalHeaderLabels(("#ID","Kitap Adı", "Yazar Adı", "Yazar Soyadı", "Durum"))
        self.ui.tableWidget_list_books.setColumnWidth(0, 50)
        self.ui.tableWidget_list_books.setColumnWidth(1, 350)
        self.ui.tableWidget_list_books.setColumnWidth(2, 350)
        self.ui.tableWidget_list_books.setColumnWidth(3, 250)
        self.ui.tableWidget_list_books.setColumnWidth(4, 250)

        counter = 0
        for i in result_search :
            self.ui.tableWidget_list_books.setItem(counter,0,QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_list_books.setItem(counter,1,QTableWidgetItem(i[1]))
            self.ui.tableWidget_list_books.setItem(counter,2,QTableWidgetItem(i[2]))
            self.ui.tableWidget_list_books.setItem(counter,3,QTableWidgetItem(i[3]))
            self.ui.tableWidget_list_books.setItem(counter,4,QTableWidgetItem(str(i[9])))
            counter += 1

        #self.ui.statusbar.showMessage(f"seçilen elamn :{result_search} ", 2000)
    ### search book END
    
    ### open rent book START
    def open_rent_book_page(self) :
        self.rentBook.show()
        self.rentBook.get_book_list()
    ### open rent book END


        

        





      




