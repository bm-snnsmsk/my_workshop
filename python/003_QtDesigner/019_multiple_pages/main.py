from PyQt5.QtWidgets import *
import sys
from main_page import Ui_anapencere
from secondPage import SecondPage
from thirdPage import ThirdPage




class MainPage(QMainWindow) :
    def __init__(self) :
        super(MainPage, self).__init__()
        self.ui = Ui_anapencere()
        self.ui.setupUi(self)

        self.secondPage = SecondPage()
        self.thirdPage = ThirdPage()

        self.ui.pushButton_pass_to_secondpage.clicked.connect(self.passToSecondPage)
        self.ui.pushButton_pass_to_third_page.clicked.connect(self.passToThirdPage)

        self.secondPage.second_page_go_home_signal.connect(self.from_second_page_go_home)
        self.thirdPage.third_page_go_home_signal.connect(self.from_third_page_go_home)

    def passToSecondPage(self) :
        self.secondPage.show()
        self.close()

    def passToThirdPage(self) :
        self.thirdPage.show()
        self.close()

    ###---------------- signal ------------------###
    def from_second_page_go_home(self) :
        self.secondPage.close()
        self.show()

    def from_third_page_go_home(self, name) :
        self.thirdPage.close()
        self.ui.statusbar.showMessage("Butonuın adı : "+name, 2000)
        self.show() 
    ###---------------- signal ------------------###



def app() :
    app = QApplication(sys.argv)
    win = MainPage()
    win.show()
    sys.exit(app.exec_())
        
app()        

        