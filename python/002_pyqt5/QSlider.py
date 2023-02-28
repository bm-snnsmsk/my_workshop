import sys
from PyQt5.QtWidgets import QWidget, QApplication,  QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QLabel, QPushButton, QScrollArea, QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self, val) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QScrollArea()")
        self.setGeometry(200, 200, 500, 500)
        self.initUI(val)
    
    def initUI(self, val) :
       layout = QVBoxLayout()
       formLayout = QFormLayout()
       groupBox = QGroupBox("This is goup box")

       labelList = []
       butonList = []

       for i in range(val) :
           labelList.append(QLabel("Label"))
           butonList.append(QPushButton("clicked me"))
           formLayout.addRow(labelList[i], butonList[i])

       


       groupBox.setLayout(formLayout)  
       scroll = QScrollArea()
       scroll.setWidget(groupBox)
       scroll.setWidgetResizable(True)
       scroll.setFixedHeight(400)


       layout.addWidget(scroll)
       self.setLayout(layout)

  

def window() :
    app = QApplication(sys.argv)
    win = MainForm(20)
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
