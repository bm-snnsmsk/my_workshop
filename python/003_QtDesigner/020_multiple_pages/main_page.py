from PyQt5.QtWidgets import *
from mainwindow import Ui_MainWindow
from addNewUser import NewPerson


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_add_new_user.clicked.connect(self.open_add_new_person_page)

        self.newPerson = NewPerson()
        self.newPerson.new_user_signal.connect(self.add_new_person_name)

    def open_add_new_person_page(self) :
        self.newPerson.show()
        self.close()       

    def add_new_person_name(self, name) :
        self.ui.comboBox_users.addItem(name)
        ## self.newPerson.ui.lineEdit_name.clear() ## diğer class'ta ayrıca bir fonksiyon (clear_lineEdit()) oluşturmaya gerek yoktu
        self.newPerson.clear_lineEdit()
        self.newPerson.close()
        self.show()



        