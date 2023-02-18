from PyQt5.QtWidgets import *
from second_page import Ui_Form





class SecondPage(QWidget) :
    def __init__(self) :
        super(SecondPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

