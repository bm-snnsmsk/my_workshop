from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
from statusbar import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_red.triggered.connect(self.selected_red)
        self.ui.action_blue.triggered.connect(self.selected_blue)
        self.ui.action_yellow.triggered.connect(self.selected_sari)
        self.ui.action_black.triggered.connect(self.selected_siyah)
        self.ui.action_green.triggered.connect(self.selected_yesil)

        self.ui.action_white.toggled[bool].connect(self.selected_beyaz)

        self.show_duration = 1500
        

    def selected_red(self) :
        self.ui.frame.setStyleSheet("border-image: url(:/icons/red.ico);")
        self.ui.statusbar.showMessage("Kırmızı kuş",self.show_duration)
        self.ui.statusbar.setStyleSheet("color:#ff0000")

    def selected_blue(self) :
        self.ui.frame.setStyleSheet("border-image: url(:/icons/blue.ico);")
        self.ui.statusbar.showMessage("Mavi kuş",self.show_duration)
        self.ui.statusbar.setStyleSheet("color:#0000ff")

    def selected_sari(self) :
        self.ui.frame.setStyleSheet("border-image: url(:/icons/yellow.ico);")
        self.ui.statusbar.showMessage("Sarı kuş",self.show_duration)
        self.ui.statusbar.setStyleSheet("color:#ffff00")

    def selected_siyah(self) :
        self.ui.frame.setStyleSheet("border-image: url(:/icons/black.ico);")
        self.ui.statusbar.showMessage("Siyah kuş",self.show_duration)
        self.ui.statusbar.setStyleSheet("color:#000000")

    def selected_yesil(self) :
        self.ui.frame.setStyleSheet("border-image: url(:/icons/green.ico);")
        self.ui.statusbar.showMessage("Yeşil kuş",self.show_duration)
        self.ui.statusbar.setStyleSheet("color:#00ff00")

    def selected_beyaz(self, val) :
        if val :
            self.ui.action_white.setIcon(QIcon(":/icons/black.ico"))
            self.ui.action_white.setIconText("Siyah")
            self.ui.action_white.setToolTip("Siyah")
            self.ui.frame.setStyleSheet("border-image: url(:/icons/white.ico);")
            self.ui.statusbar.showMessage("Beyaz kuş",self.show_duration)
            self.ui.statusbar.setStyleSheet("color:#ffffff")
        else:             
            self.ui.action_white.setIcon(QIcon(":/icons/white.ico"))
            self.ui.action_white.setIconText("Beyaz")
            self.ui.action_white.setToolTip("Beyaz")
            self.ui.frame.setStyleSheet("border-image: url(:/icons/black.ico);")
            self.ui.statusbar.showMessage("Siyah kuş",self.show_duration)
            self.ui.statusbar.setStyleSheet("color:#000000")
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


