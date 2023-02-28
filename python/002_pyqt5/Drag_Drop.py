import sys
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon

class MainWindow(QWidget) :
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("QTimeEdit()")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(200, 200, 500, 300)
        self.initUI()

    def initUI(self) :
       hbox = QHBoxLayout()

       self.listwidget_1 = QListWidget()
       self.listwidget_2 = QListWidget()
       self.listwidget_2.setViewMode(QListWidget.IconMode)
       self.listwidget_1.setAcceptDrops(True)
       self.listwidget_1.setDragEnabled(True)
       self.listwidget_2.setAcceptDrops(True)
       self.listwidget_2.setDragEnabled(True)
       
       l1 = QListWidgetItem(QIcon("close.ico"), "close")
       l2 = QListWidgetItem(QIcon("icon.png"), "icon")
       l3 = QListWidgetItem(QIcon("icon.jpg"), "icon")

       self.listwidget_1.insertItem(1, l1)
       self.listwidget_1.insertItem(2, l2)
       self.listwidget_1.insertItem(3, l3)

       QListWidgetItem(QIcon("icon.jpg"), "jpg", self.listwidget_2)
       QListWidgetItem(QIcon("icon.png"), "png", self.listwidget_2)
       QListWidgetItem(QIcon("close.ico"), "close", self.listwidget_2)
    


       hbox.addWidget(self.listwidget_1)
       hbox.addWidget(self.listwidget_2)
       self.setLayout(hbox)





def window() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) # x ile kapatılabilme

window()
