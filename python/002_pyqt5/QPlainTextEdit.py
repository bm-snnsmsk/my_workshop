import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPlainTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTime

class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QPlainTextEdit()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 600, 250)
        self.initUI()

    def initUI(self) :
       vbox = QVBoxLayout()

       plaintextwidget = QPlainTextEdit() 
       plaintextwidget.setPlaceholderText("Bu QPlainTextEdit için bir placeholder örneğidir")
    #    plaintextwidget.setReadOnly(True)
       text = "Text örneği"
       plaintextwidget.appendPlainText(text)
       plaintextwidget.setUndoRedoEnabled(False) ## geri alma pasife alındı

       vbox.addWidget(plaintextwidget) 
       self.setLayout(vbox)



def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
