from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal
from add_book import Ui_MainWindow

from data_base import DataBase





class AddBook(QMainWindow) :
    add_book_signal = pyqtSignal(str, str, str, str, str, str, str, str)
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ### initial edits START
        font = QFont()
        font.setPointSize(14)
        self.ui.textEdit_description.setFont(font)
        ### initial edits END
        
        self.ui.pushButton_add_book.clicked.connect(self.add_new_book)

        self.db = DataBase('library.db')

        ### category combobox'a elemanlar eklendi START
        categories = self.db.getDatas('select * from categories')['data']
        for i in categories :
            self.ui.comboBox_category.addItem(str(i[1]))
        ### category combobox'a elemanlar eklendi END


    def add_new_book(self) :
        book_name = self.ui.lineEdit_book_name.text()
        author_first_name = self.ui.lineEdit_author_first_name.text()
        author_last_name = self.ui.lineEdit_author_last_name.text()
        category = self.ui.comboBox_category.currentText()
        publisher = self.ui.lineEdit_publisher.text()
        page_count = self.ui.lineEdit_page_count.text()
        language = self.ui.lineEdit_language.text()
        description = self.ui.textEdit_description.toPlainText()
        self.add_book_signal.emit(book_name, author_first_name, author_last_name, category, publisher, page_count, language, description)

    def clear_add_book_form(self) :
        self.ui.lineEdit_book_name.setText("")
        self.ui.lineEdit_book_name.setFocus(True)
        self.ui.lineEdit_author_first_name.setText("")
        self.ui.lineEdit_author_last_name.setText("")
        self.ui.comboBox_category.setCurrentIndex(-1)
        self.ui.lineEdit_book_name.setText("")
        self.ui.lineEdit_publisher.setText("")
        self.ui.lineEdit_page_count.setText("")
        self.ui.lineEdit_language.setText("")
        self.ui.textEdit_description.setText("")

    
    