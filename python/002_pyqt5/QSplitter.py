import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QFrame, QSplitter, QLineEdit
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QSplitter()")
        self.setGeometry(200, 200, 500, 500)
        self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
       hbox = QHBoxLayout()

       left_frame = QFrame()
       left_frame.setFrameShape(QFrame.StyledPanel)

       bottom_frame = QFrame()
       bottom_frame.setFrameShape(QFrame.StyledPanel)

       splitter1 = QSplitter(Qt.Horizontal)

       lineedit = QLineEdit()
       lineedit.setStyleSheet("background-color:green")

       splitter1.addWidget(left_frame)
       splitter1.addWidget(lineedit)
       splitter1.setSizes([200,200])
       splitter1.setStyleSheet("background-color:blue")

       splitter2 = QSplitter(Qt.Vertical)
       splitter2.addWidget(splitter1)
       splitter2.addWidget(bottom_frame)
       splitter2.setStyleSheet("background-color:pink")

       hbox.addWidget(splitter2)

       self.setLayout(hbox)

 

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
