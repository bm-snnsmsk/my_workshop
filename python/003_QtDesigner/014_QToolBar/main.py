from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sys
from toolbar import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_kirmizi.triggered.connect(self.selected_red)
        self.ui.action_blue.triggered.connect(self.selected_blue)
        self.ui.action_sari.triggered.connect(self.selected_sari)
        self.ui.action_siyah.triggered.connect(self.selected_siyah)
        self.ui.action_yesil.triggered.connect(self.selected_yesil)
        self.ui.actionBeyaz.toggled[bool].connect(self.selected_beyaz)

        self.ui.label_aciklama.setText("seçim yok")
        self.ui.label_aciklama.setStyleSheet("background-color:#acacac; color: #ffffff; font-weight:bold")

    def selected_red(self) :
        #renk = self.sender().text()
        self.ui.label_aciklama.setText("kırmızı kuş")
        self.ui.label_aciklama.setStyleSheet("background-color:#ff0000; color: #ffffff; font-weight:bold")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/red.ico);")
        #self.ui.frame_show.setStyleSheet("border-image: url(:/icons/"+renk+".ico);")
    def selected_blue(self) :
        self.ui.label_aciklama.setText("mavi kuş")
        self.ui.label_aciklama.setStyleSheet("background-color:#0000ff; color: #ffffff; font-weight:bold")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/blue.ico);")

    def selected_sari(self) :
        self.ui.label_aciklama.setText("sarı kuş")
        self.ui.label_aciklama.setStyleSheet("background-color:#ffff00; color: #ffffff; font-weight:bold")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/yellow.ico);")

    def selected_siyah(self) :
        self.ui.label_aciklama.setText("siyah kuş")
        self.ui.label_aciklama.setStyleSheet("background-color:#000000; color: #ffffff; font-weight:bold")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/black.ico);")

    def selected_yesil(self) :
        self.ui.label_aciklama.setText("yeşil kuş")
        self.ui.label_aciklama.setStyleSheet("background-color:#00ff00; color: #ffffff; font-weight:bold")
        self.ui.frame_show.setStyleSheet("border-image: url(:/icons/green.ico);")

    def selected_beyaz(self, val) :
        if val :
            self.ui.label_aciklama.setText("beyaz kuş")
            self.ui.actionBeyaz.setIcon(QIcon(":/icons/black.ico"))
            self.ui.actionBeyaz.setIconText("Siyah")
            self.ui.actionBeyaz.setToolTip("Siyah")
            self.ui.label_aciklama.setStyleSheet("background-color:#ffffff; color: #000; font-weight:bold")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/white.ico);")
        else: 
            self.ui.label_aciklama.setText("siyah kuş")
            self.ui.actionBeyaz.setIcon(QIcon(":/icons/white.ico"))
            self.ui.actionBeyaz.setIconText("Beyaz")
            self.ui.actionBeyaz.setToolTip("Beyaz")
            self.ui.label_aciklama.setStyleSheet("background-color:#000; color: #fff; font-weight:bold")
            self.ui.frame_show.setStyleSheet("border-image: url(:/icons/black.ico);")
    


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


