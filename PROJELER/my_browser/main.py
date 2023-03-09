import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class MainWindow(QMainWindow) :
    
    def __init__(self) :
        super().__init__()
        self.setGeometry(200,200,900,600)
        self.setWindowTitle("PyBrowser")
        self.setWindowIcon(QIcon("network.ico"))
        self.initialUrl = "https://google.com"

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("home.ico"))
        self.homeButton.setIconSize(QSize(36,36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("backward.ico"))
        self.backButton.setIconSize(QSize(36,36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("reload.ico"))
        self.reloadButton.setIconSize(QSize(36,36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("forward.ico"))
        self.forwardButton.setIconSize(QSize(36,36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Arial",18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)
        
        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("search.ico"))
        self.searchButton.setIconSize(QSize(36,36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)        
        self.addressLineEdit.setText(self.initialUrl)
        self.webEngineView.load(QUrl(self.initialUrl))
    
    def searchBtn(self) :
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))
    
    def backBtn(self) :
        self.webEngineView.back()
    
    def forwardBtn(self) :
        self.webEngineView.forward()
   
    def reloadBtn(self) :
        self.webEngineView.reload()
   
    def homeBtn(self) :
        self.webEngineView.load(QUrl(self.initialUrl))




    


def applicaion() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

applicaion()