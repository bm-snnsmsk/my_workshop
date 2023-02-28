import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QTableWidget()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       tablewidget = QTableWidget() 
       tablewidget.setRowCount(5)
       tablewidget.setColumnCount(3)

       tablewidget.setHorizontalHeaderLabels(("Name", "Phone","Email")) 
       tablewidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

       tablewidget.setItem(0, 0, QTableWidgetItem("Sinan"))
       tablewidget.setItem(0, 1, QTableWidgetItem("5444494263"))
       tablewidget.setItem(0, 2, QTableWidgetItem("bm.snn@gmail.com"))

       tablewidget.setItem(1, 0, QTableWidgetItem("baran"))
       tablewidget.setItem(1, 1, QTableWidgetItem("2222222"))
       tablewidget.setItem(1, 2, QTableWidgetItem("baran@gmail.com"))

       tablewidget.setItem(1, 0, QTableWidgetItem("emine"))
       tablewidget.setItem(1, 1, QTableWidgetItem("3434343"))
       tablewidget.setItem(1, 2, QTableWidgetItem("eminen@gmail.com"))

       vbox.addWidget(tablewidget) 
       self.setLayout(vbox)



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
