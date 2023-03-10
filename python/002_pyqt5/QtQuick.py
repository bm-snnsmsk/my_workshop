import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtQml import QQmlApplicationEngine

def runQML() :
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    app.setWindowIcon(QIcon("home.png"))
    engine.load("main.qml")

    if not engine.rootObjects():
        return -1
    
    return app.exec_()

if __name__ == "__main__" :
    sys.exit(runQML())