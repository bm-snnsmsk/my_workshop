import sys
from PyQt5.QtWidgets import QApplication
from renkPaleti import MainWindow






def application() :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

application()