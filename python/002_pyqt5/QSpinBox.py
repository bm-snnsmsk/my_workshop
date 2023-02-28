import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QSpinBox, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QSpinBox()")
        self.setGeometry(200, 200, 500, 500)
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_changed)
        


        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def spin_changed(self) :
        getValue = self.spinbox.value()
        self.label.setText("spin değeri : "+ str(getValue))

       
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
