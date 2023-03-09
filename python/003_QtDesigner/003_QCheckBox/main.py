from PyQt5 import QtWidgets
import sys
from _checkbox import Ui_MainWindow



class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## change için fonksiyon yazıldı ama içerisi doldurulmadı  START
        self.ui.cbox_kitap.stateChanged.connect(self.show_state)
        self.ui.cbox_sinema.stateChanged.connect(self.show_state)
        self.ui.cbox_spor.stateChanged.connect(self.show_state)
        self.ui.cbox_spor.setChecked(True)



        self.ui.cbox_csharp.stateChanged.connect(self.show_state)
        self.ui.cbox_javascript.stateChanged.connect(self.show_state)
        self.ui.cbox_python.stateChanged.connect(self.show_state)
        ## change için fonksiyon yazıldı ama içerisi doldurulmadı END

        self.ui.btn_hobileri_gonder.clicked.connect(self.hobileri_gonder)
        # self.ui.btn_dilleri_gonder.clicked.connect(self.dilleri_gonder)
        self.ui.btn_dilleri_gonder.toggled.connect(self.dilleri_gonder) ## toggled = clicked 

    def show_state(self, value) :
        # print(value) ## seçili değilse 0, seçili ise 2
        # print(self.ui.cbox_kitap.isChecked()) ## True, False
        # print(self.ui.cbox_kitap.text())   ## cbox üzerindeki text

        ## bunların yerine her checbox için geçerli olacak bir işlem gerekli
        # cbox = self.sender()
        # print(cbox.text())
        pass

    def hobileri_gonder(self) :
        # all_cbox = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) ## ana penceredeki tüm cbox'ları al
        all_cbox = self.ui.gbox_hobiler.findChildren(QtWidgets.QCheckBox) ## gbox_hobiler groupBox içindeki tüm cbox'ları al
        # print(all_cbox) ## bir liste geriye döndürür 
        txt = ""
        for i in all_cbox :
            if i.isChecked() :
                print(i.text())
                txt += i.text()+"\n"
               
        self.ui.lbl_hobiler_sonuc.setText(txt)

    def dilleri_gonder(self) :
        # all_cbox = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox) ## ana penceredeki tüm cbox'ları al
        all_cbox = self.ui.gbox_diller.findChildren(QtWidgets.QCheckBox) ## gbox_diller groupBox içindeki tüm cbox'ları al
        # print(all_cbox) ## bir liste geriye döndürür 
        txt = ""
        for i in all_cbox :
            if i.isChecked() :
                print(i.text())
                txt += i.text()+"\n"
               
        self.ui.lbl_diller_sonuc.setText(txt)

       
       

def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_()) 
    

app()


