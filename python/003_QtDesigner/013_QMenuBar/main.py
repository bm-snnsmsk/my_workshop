from PyQt5 import QtWidgets
import sys
from untitled import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionblack.triggered.connect(self.selected_black)
        self.ui.actionred.triggered.connect(self.selected_red)
        self.ui.actionwhite.triggered.connect(self.selected_white)
        self.ui.actionyellow.triggered.connect(self.selected_yellow)

    def selected_black(self) :
        print("siyah renk seçildi")
    def selected_red(self) :
        print("red renk seçildi")
    def selected_white(self) :
        print("beyaz renk seçildi")
    def selected_yellow(self) :
        print("yellow renk seçildi")


        


    

  

      
        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


