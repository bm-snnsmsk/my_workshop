from PyQt5.QtWidgets import *
from third_page import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal




class ThirdPage(QMainWindow) :
    third_page_go_home_signal = pyqtSignal(str)
    def __init__(self) :
        super(ThirdPage, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_third_go_home_pge.clicked.connect(self.go_home_page)

    def go_home_page(self) :
        isim = self.ui.pushButton_third_go_home_pge.text()
        self.third_page_go_home_signal.emit(isim)
