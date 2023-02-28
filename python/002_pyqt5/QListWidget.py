import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QListWidget, QLabel
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QListWidget()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       self.list = QListWidget()
       self.list.insertItem(0,"python")
       self.list.insertItem(1,"C++")
       self.list.insertItem(2,"C#")
       self.list.insertItem(3,"java")
       self.list.insertItem(4,"rugby")
       self.list.insertItem(5,"kotlin")

       self.list.clicked.connect(self.listview_clicked)
       
       self.label = QLabel()
       self.label.setFont(QFont("Sanserif",15))

       vbox.addWidget(self.label)
       vbox.addWidget(self.list)
       self.setLayout(vbox)

    def listview_clicked(self) :
        item = self.list.currentItem()
        self.label.setText(str(item.text()))



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
