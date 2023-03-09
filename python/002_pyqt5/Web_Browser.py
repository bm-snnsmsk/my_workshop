import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngineWidgets import *  ## pip install PyQtWebEngine


app = QApplication(sys.argv)
web = QWebEngineView()
web.load(QUrl("https://google.com"))
web.show()
sys.exit(app.exec_()) # x ile kapatılabilme
