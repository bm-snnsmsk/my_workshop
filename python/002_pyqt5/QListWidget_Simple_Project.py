import sys
from PyQt5.QtWidgets import QDialog, QApplication,QLineEdit, QInputDialog, QMessageBox, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QDialog) :
    def __init__(self, name, proList = None) :
        super().__init__()
        self.setWindowTitle("QListWidget_Simple_Project()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
              
        self.name = name
        self.list = QListWidget()

        if proList is not None :
            self.list.addItems(proList)
            self.list.setCurrentRow(0)

        vbox = QVBoxLayout()

        for text, slot in (("Add", self.add), 
                           ("Edit", self.edit), 
                           ("Remove", self.remove), 
                           ("Sort", self.sort), 
                           ("Close", self.close)) :
            buttons = QPushButton(text)
            buttons.clicked.connect(slot)
            vbox.addWidget(buttons)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox)
        self.setLayout(hbox)

    def add(self) :
        row = self.list.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string is not None :
            self.list.insertItem(row, string)


    def edit(self) :
        row = self.list.currentRow()
        item = self.list.item(row)
        if item is not None :
            title = "Edit {} ".format(self.name)
            string, ok = QInputDialog.getText(self, title, title, QLineEdit.Normal, item.text())
            if ok and string is not None :
                item.setText(string)

    def remove(self) :
        row = self.list.currentRow()
        item = self.list.item(row)
        if item is None :
            return
        reply = QMessageBox.question(self, "Remove {0}".format(self.name), "Remove {0} '{1}' ?".format(self.name, item.text()), QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes :
            item = self.list.takeItem(row)
            del item
    
        


    def sort(self) :
        self.list.sortItems()

    def close(self) :
        self.accept()






def window() :
    app = QApplication(sys.argv)
    programing = ["python","java","C#", "C++","Ruby","Kotlin"]
    win = MainWindow("Diller",programing)
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
