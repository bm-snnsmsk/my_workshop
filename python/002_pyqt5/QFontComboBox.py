import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout,QLabel, QFontComboBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainForm(QWidget) :
    def __init__(self) :
        super(MainForm, self).__init__()
        self.setWindowTitle("QFontComboBox()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 500, 500)
        # self.setStyleSheet("background-color:yellow")
        self.initUI()
    
    def initUI(self) :
        vbox = QVBoxLayout()

        font_combo = QFontComboBox()
        font_combo.setFontFilters(QFontComboBox.MonospacedFonts)


        vbox.addWidget(font_combo)
        self.setLayout(vbox)

        
        
       
  

def window() :
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
