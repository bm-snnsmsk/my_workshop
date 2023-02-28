from PyQt5.QtWidgets import *
from second_page import Ui_Form
from PyQt5.QtCore import pyqtSignal




class SecondPage(QWidget) :
    second_page_go_home_signal = pyqtSignal()
    def __init__(self) :
        super(SecondPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton_second_go_home_pge.clicked.connect(self.go_home_page)

    def go_home_page(self) :
        self.second_page_go_home_signal.emit()


