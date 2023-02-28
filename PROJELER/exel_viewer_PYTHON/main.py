from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5 import QtCore
import sys
from todo import Ui_MainWindow



class MainWindow(QMainWindow) :
    def __init__(self) :
        super().__init__() 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_toogle_all.clicked.connect(self.toggle_all)

        todos = ["walk dog", "go to shopping","send email","call bank","clean house"]
        for i in todos :
            item = QListWidgetItem(i)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked) ## Checked
            self.ui.listWidget_todo.addItem(item)
    
    def toggle_all(self) :
        for i in range(self.ui.listWidget_todo.count()) :
            item = self.ui.listWidget_todo.item(i)
            if item.checkState() == QtCore.Qt.Checked :
                item.setCheckState(QtCore.Qt.Unchecked)
            else :
                item.setCheckState(QtCore.Qt.Checked)



def app() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) ## bu satır sonsuz bir döngü sağlar

app()






    
    
