import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QWizard, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QWizard()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       self.wizard = QWizard() 
       self.wizard.setWindowTitle("Launching...")
       button = QPushButton("Open Wizard") 
       button.clicked.connect(self.btn_clicked)


       vbox.addWidget(button) 
       self.setLayout(vbox)
    
    def btn_clicked(self) :
        self.wizard.open()



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
