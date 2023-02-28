from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from add_user import Ui_MainWindow




class AddUser(QMainWindow) :
    add_user_signal = pyqtSignal(str, str, str, str, str)
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton_add_user.clicked.connect(self.add_new_user)
        self.ui.pushButton_resim_ekle.clicked.connect(self.select_user_photo)
        self.user_photo = ""
        
        
    def select_user_photo(self) :
        pass

    def add_new_user(self) :
        user_first_name = self.ui.lineEdit_user_first_name.text()
        user_last_name = self.ui.lineEdit_user_last_name.text()
        user_email = self.ui.lineEdit_user_email.text()
        user_phone_number = self.ui.lineEdit_user_telefon.text()
        user_photo = self.user_photo
        self.add_user_signal.emit(user_first_name, user_last_name, user_email, user_phone_number, user_photo)

    def clear_add_user_form(self) :
        self.user_photo = ""

    
    