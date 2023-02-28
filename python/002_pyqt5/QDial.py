import sys
from PyQt5.QtWidgets import QWidget, QApplication,  QVBoxLayout, QLabel, QDial
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QDial()")
        self.setGeometry(200, 200, 500, 500)
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()
        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_changed)

        self.label = QLabel(self)
        self.label.setFont(QFont("Sanserif", 15))


        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def dial_changed(self) :
        getValue = self.dial.value()
        self.label.setText("dial değeri : "+ str(getValue))

       
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
