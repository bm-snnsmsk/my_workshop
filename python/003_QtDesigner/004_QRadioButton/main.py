from PyQt5 import QtWidgets
import sys
from radiobutton import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_egitim_sec.clicked.connect(self.egitim_sec)
        self.ui.btn_ulke_sec.clicked.connect(self.ulke_sec)

        self.ui.r_btn_abd.setChecked(True) ## varsayılan seçmek
        self.ui.r_btn_ilkokul.setChecked(True) ## varsayılan seçmek

        self.ui.r_btn_abd.toggled.connect(self.ulke_tikla)
        self.ui.r_btn_almanya.toggled.connect(self.ulke_tikla)
        self.ui.r_btn_ingiltere.toggled.connect(self.ulke_tikla)
        self.ui.r_btn_rusya.toggled.connect(self.ulke_tikla)

        self.ui.r_btn_ilkokul.toggled.connect(self.egitim_tikla)
        self.ui.r_btn_lise.toggled.connect(self.egitim_tikla)
        self.ui.r_btn_universite.toggled.connect(self.egitim_tikla)
        self.ui.r_btn_yuksek_lisans.toggled.connect(self.egitim_tikla)

        

    def egitim_sec(self) :
        all_radio_btn = self.ui.gbox_egitim.findChildren(QtWidgets.QRadioButton)  
        txt = ""
        for i in all_radio_btn :
            if i.isChecked() :
                txt += i.text()
        self.ui.lbl_egitim.setText(txt)

    def ulke_sec(self) :
        all_radio_btn = self.ui.gbox_ulkeler.findChildren(QtWidgets.QRadioButton)  
        txt = ""
        for i in all_radio_btn :
            if i.isChecked() :
                txt += i.text()
        self.ui.lbl_ulkeler.setText(txt)


    def ulke_tikla(self) :
        radio_btn = self.sender() ## seçili radio butonu yakalamak
        if radio_btn.isChecked() : ## True False
            print("Seçilen Ulke : "+radio_btn.text())

    def egitim_tikla(self) :
        radio_btn = self.sender() ## seçili radio butonu yakalamak
        if radio_btn.isChecked() : ## True False
            print("Eğitim durumu : "+radio_btn.text())


        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_()) 
    

app()


