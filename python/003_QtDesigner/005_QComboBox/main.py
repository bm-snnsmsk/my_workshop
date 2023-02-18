from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from combobox import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # liste = ["adana","van"]
        # self.ui.cbox_sehirler.addItem("İstanbul")
        # self.ui.cbox_sehirler.addItems(liste)
        # self.ui.cbox_sehirler.addItems(["muş","bitlis"])

        self.ui.btn_sehir_ekle.clicked.connect(self.sehir_ekle)
        self.ui.btn_sehir_sec.clicked.connect(self.sehir_sec)
        self.ui.btn_sehir_temizle.clicked.connect(self.sehir_temizle)

        self.ui.cbox_sehirler.currentIndexChanged.connect(self.selectedChangedIndex) ## = currentIndexChanged[int]
        self.ui.cbox_sehirler.currentIndexChanged[str].connect(self.selectedChangedText)
        

        ## bu şekilde eleman sona eklenir
        self.ui.cbox_hayvanlar.addItem("kanarya", 100)
        self.ui.cbox_hayvanlar.addItem(QIcon(":/img/red.ico"),"şahin", 101)
        self.ui.cbox_hayvanlar.addItem(QIcon(":/img/blue.ico"),"papağan", 102)
        self.ui.cbox_hayvanlar.addItem("güvercin", 103)
        self.ui.cbox_hayvanlar.currentIndexChanged.connect(self.fff)

 
        




        ## çoğul durumlarda icon ekleme yapılamıyor
        self.ui.cbox_arabalar.addItems(["fiat","corolla","tofaş"])
        self.ui.cbox_arabalar.insertItem(0,QIcon(":/img/start.ico"),"Araba Markası Seçiniz",201)
        self.ui.cbox_arabalar.insertItem(2,"Toyota")
        self.ui.cbox_arabalar.setCurrentIndex(0)
        self.ui.cbox_arabalar.highlighted[int].connect(self.hightlight_fonk) ## item üzerindeki hover fonksiyonu

        ## meyveler
        self.ui.cbox_meyveler.addItem("elma")
        self.ui.cbox_meyveler.addItem("portakal")
        self.ui.cbox_meyveler.addItem("çilek")
        self.ui.cbox_meyveler.addItem("armut")

        self.ui.cbox_meyveler.activated[int].connect(self.aktivate_fonksiyon)
    def aktivate_fonksiyon(self, val) :## aynı item'a basılsa bile aktifleşen bir fonksiyon ama currentIndexChanged ise illa farklı bir indexe tıklanması lazım
        print(val)
        self.ui.cbox_hayvanlar.removeItem(val)

    def fff(self, index) :
        print(index, self.ui.cbox_hayvanlar.itemText(index))



      

        

    def hightlight_fonk(self, index) : ## text = seçilen elemanın text bilgisi
        print(index)
        

    def selectedChangedText(self, text) : ## text = seçilen elemanın text bilgisi
        print(text)
        print("self.ui.cbox_hayvanlar.currentData() : "+ str(self.ui.cbox_hayvanlar.currentData())) ## 
        self.ui.cbox_hayvanlar.showPopup()

    def selectedChangedIndex(self, index) : ## index = seçilen elemanın index bilgisi
        print(index)

    def sehir_ekle(self) :
        sehirler = ["adana","van","muş","bitlis","hakkari"]
        self.ui.cbox_sehirler.addItems(sehirler)

    def sehir_sec(self) :
        print(self.ui.cbox_sehirler.currentText())
        print(self.ui.cbox_sehirler.currentIndex())
        print(self.ui.cbox_sehirler.count())  ## toplam liste elemnı

        for i in range(self.ui.cbox_sehirler.count()) :
            print(self.ui.cbox_sehirler.itemText(i))

    def sehir_temizle(self) :        
        self.ui.cbox_sehirler.clear()


    

       


        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


