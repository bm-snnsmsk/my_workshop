import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QFileDialog, QPushButton, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QTime

class MainWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QFileDialog()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       self.btn =  QPushButton("Browse Image")
       self.btn.clicked.connect(self.browseImage)
       
       self.label =  QLabel("Hello")

       vbox.addWidget(self.btn) 
       vbox.addWidget(self.label) 
       self.setLayout(vbox)
    
    def browseImage(self) :
        fname = QFileDialog.getOpenFileName(self, "Open File", "c\\" , "Image Files (*.jpg *.gif)")
        imagepath = fname[0]
        pixmap = QPixmap(imagepath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(pixmap.width(), pixmap.height())



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
