from PyQt5.QtWidgets import *
from third_page import Ui_MainWindow





class ThirdPage(QMainWindow) :
    def __init__(self) :
        super(ThirdPage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
