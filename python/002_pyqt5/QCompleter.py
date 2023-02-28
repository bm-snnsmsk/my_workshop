import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QCompleter, QLineEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QCompleter()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()
       names = ["Afghanistan","india","pakistan","china","uea","america"]
       completer = QCompleter(names)

       self.lineedit = QLineEdit()
       self.lineedit.setCompleter(completer)
       vbox.addWidget(self.lineedit)

       self.setLayout(vbox)




def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
