import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QFrame

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QFrame()")
        self.setGeometry(200, 200, 500, 500)
        self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
       hbox = QHBoxLayout()
       frame = QFrame()
       frame.setFrameShape(QFrame.StyledPanel)
       frame.setStyleSheet("background-color:red")
       hbox.addWidget(frame)

       self.setLayout(hbox)

 

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
