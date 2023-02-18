from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from table_widget import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btn_ekle.clicked.connect(self.urun_ekle)
        self.ui.tableWidget.doubleClicked.connect(self.urun_duzenle)
       
   
    def urun_duzenle(self) :
        print(self.ui.tableWidget.selectedItems())
        # print(self.ui.tableWidget.selectedIndexes())
        # for i in self.ui.tableWidget.selectedIndexes() :
        #     print(i.row(), i.column())
        for i in self.ui.tableWidget.selectedItems() :
            print(i.text(),i.row(), i.column())

    def urun_ekle(self) :
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()
        index = self.ui.tableWidget.currentRow() ## 0
        index1 = self.ui.tableWidget.rowCount() ## en son index + 1
        print(index)
        print(index1)

        if name and price is not None :
            self.ui.tableWidget.insertRow(index1) ## sona eleman eklendiğinde bu gerekli aksi takdirde index1 sayılı index olmadığından ekleme yapamayacaktır
            self.ui.tableWidget.setItem(index1,0,QTableWidgetItem(name))
            self.ui.tableWidget.setItem(index1,1,QTableWidgetItem(price))

        self.ui.txt_name.setText("")
        self.ui.txt_price.setText("")



    def loadProducts(self) :

        products = [
            {"name":"İphone X", "price" : 11000},
            {"name":"İphone 11", "price" : 13000},
            {"name":"İphone 12", "price" : 17000},
            {"name":"İphone 13", "price" : 31000}
        ]



        self.ui.tableWidget.setRowCount(len(products))
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(("Ürün Adı","Fiyat"))
        self.ui.tableWidget.setColumnWidth(0, 250)
        self.ui.tableWidget.setColumnWidth(1, 75)


        ######## Tek Tek veri ekleme
        # self.ui.tableWidget.setItem(0,0,QTableWidgetItem("Samsung S5"))
        # self.ui.tableWidget.setItem(0,1,QTableWidgetItem("7000"))

        # self.ui.tableWidget.setItem(1,0,QTableWidgetItem("Samsung S3"))
        # self.ui.tableWidget.setItem(1,1,QTableWidgetItem("2000"))

        # self.ui.tableWidget.setItem(2,0,QTableWidgetItem("Samsung S12"))
        # self.ui.tableWidget.setItem(2,1,QTableWidgetItem("20000"))


        ## Dinamik veri ekleme
        counter = 0
        for i in products :
            self.ui.tableWidget.setItem(counter,0,QTableWidgetItem(i["name"]))
            self.ui.tableWidget.setItem(counter,1,QTableWidgetItem(str(i["price"])))
            counter += 1



   
    

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


