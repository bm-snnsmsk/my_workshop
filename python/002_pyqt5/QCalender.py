import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QCalender()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 400, 300)
        self.initUI()

    def initUI(self) :
        vbox = QVBoxLayout()
 
        self.calender = QCalendarWidget() 
        self.calender.setGridVisible(True)
        self.calender.selectionChanged.connect(self.onSelectedChanged)
 
        self.label = QLabel()
        self.label.setFont(QFont("Sanserif",15))
        self.label.setStyleSheet("color:green")
        
 
        vbox.addWidget(self.calender) 
        vbox.addWidget(self.label) 
        self.setLayout(vbox)

    def onSelectedChanged(self) :
        ca = self.calender.selectedDate()
        self.label.setText(str(ca))
        # self.label.setText(str(ca.day()))



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
