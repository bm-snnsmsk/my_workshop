from PyQt5.QtWidgets import *
from main_page import Ui_anapencere
from secondPage import SecondPage
from thirdPage import ThirdPage




class MainPage(QMainWindow) :
    def __init__(self) :
        super(MainPage, self).__init__()
        self.ui = Ui_anapencere()
        self.ui.setupUi(self)

        self.ui.pushButton_pass_to_secondpage.clicked.connect(self.passToSecondPage)
        self.ui.pushButton_pass_to_third_page.clicked.connect(self.passToThirdPage)

        self.secondPage = SecondPage()
        self.thirdPage = ThirdPage()

    def passToSecondPage(self) :
        self.secondPage.show()
        

    def passToThirdPage(self) :
        self.thirdPage.show()
        