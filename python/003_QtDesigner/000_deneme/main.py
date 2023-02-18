from PyQt5 import QtWidgets
import sys
from untitled import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("deneme window")
        self.resize(800,600)

        self.ui.pushButton.clicked.connect(self.tikla)

    def tikla(self) :
        self.ui.label_sonuc.setText('tklandi')






        

        

  
        

      







def app() :
    myapp = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(myapp.exec_())    

app()