from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from add_new_user import Ui_Form




class NewPerson(QMainWindow) :

    new_user_signal = pyqtSignal(str)

    def __init__(self) :
        super(NewPerson, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_add_name.clicked.connect(self.add_new_person)

    def add_new_person(self) :
        name = self.ui.lineEdit_name.text()
        #print(name)
        self.new_user_signal.emit(name)

    def clear_lineEdit(self) :
        self.ui.lineEdit_name.clear()
