from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
import sys
from list_widget import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStudent()
        self.ui.btn_add.clicked.connect(self.addStudent)
        self.ui.btn_remove.clicked.connect(self.removeStudent)
        self.ui.btn_edit.clicked.connect(self.editStudent)
        self.ui.btn_down.clicked.connect(self.downStudent)
        self.ui.btn_up.clicked.connect(self.upStudent)
        self.ui.btn_sort.clicked.connect(self.sortStudent)
        self.ui.btn_exit.clicked.connect(self.exit)

    def removeStudent(self) :
        index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index)
        if item is None :
            return
        
        q = QtWidgets.QMessageBox.question(self, "Öğrenci silme",str(item.text())+" isimli öğrenciyi silmek istediğinize Emin misiniz ?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No) ## QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No bu ikisi varsayılan olarak zaten var
        if q == QtWidgets.QMessageBox.Yes :
            item = self.ui.listWidget.takeItem(index)
            del item



    def editStudent(self) :
        index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(index)

        if item and item != "" :
            text, ok = QInputDialog.getText(self,"Öğrenci Güncelleme", "Öğrenci Adı :", QtWidgets.QLineEdit.Normal,item.text())
            if ok and text != '':                
                item.setText(text)

    def downStudent(self) :
        index = self.ui.listWidget.currentRow()
        if index < self.ui.listWidget.count() - 1 : ## toplam eleman sayısı
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index + 1, item)
            #self.ui.listWidget.setCurrentRow(index + 1) ## seçili eleman
            self.ui.listWidget.setCurrentItem(item)

    def upStudent(self) :
        index = self.ui.listWidget.currentRow()
        if index != 0 :
            item = self.ui.listWidget.takeItem(index)
            self.ui.listWidget.insertItem(index - 1, item)
            self.ui.listWidget.setCurrentItem(item) ## seçili eleman



    def sortStudent(self) :
        self.ui.listWidget.sortItems()
        self.ui.listWidget.setCurrentRow(0) ## seçili eleman

    def loadStudent(self) :
        self.ui.listWidget.addItems(["Sinan","Baran","Emine","Tubanur"])
        self.ui.listWidget.setCurrentRow(0) ## seçili eleman

    def addStudent(self) :
        ## self.ui.listWidget.addItem("Kendal")
        #newItem = QInputDialog.getText()
        index = self.ui.listWidget.currentRow() ## seçilen satır indexi
        text, okPressed = QInputDialog.getText(self, "Yeni Öğrenci","Öğrenci Adı :", QtWidgets.QLineEdit.Normal, "")
        if okPressed and text != '':
            self.ui.listWidget.addItem(text)
            self.ui.listWidget.insertItem(index,text) 

    def exit(self) :
        # result = QtWidgets.QMessageBox.question(self, "Kapatma Uygulaması", "Emin misin ?")
        # print(result)
        # if result == QtWidgets.QMessageBox.Yes :
        #     QtWidgets.qApp.quit()
        quit()

        
    
    

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


