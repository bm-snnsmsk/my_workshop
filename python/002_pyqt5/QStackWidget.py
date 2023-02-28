import sys
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QLabel, QPushButton, QStackedWidget
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

class MainWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QStackedWidget()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 300, 250)
        self.initUI()

    def initUI(self) :
        vbox = QVBoxLayout()
        self.stackedwidget = QStackedWidget()
        vbox.addWidget(self.stackedwidget)

        for i in range(0,8) :
            label = QLabel("stacked child" +str(i))
            label.setFont(QFont("Sanserif", 14))
            label.setStyleSheet("color:red")
            self.stackedwidget.addWidget(label)

            self.button = QPushButton("stack : "+str(i))
            self.button.setStyleSheet("background-color:green")
            self.button.page = i
            self.button.clicked.connect(self.btn_clicked)
            vbox.addWidget(self.button)
        
        self.setLayout(vbox)
        
    def btn_clicked(self) :
        self.button = self.sender()
        self.stackedwidget.setCurrentIndex(self.button.page - 1)







def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
