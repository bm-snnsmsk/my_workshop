# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 641)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/login.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/images/3.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 121, 71))
        self.pushButton.setStyleSheet("border-image: url(:/images/red.ico);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.listWidget_listele = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_listele.setGeometry(QtCore.QRect(130, 290, 451, 331))
        self.listWidget_listele.setObjectName("listWidget_listele")
        self.label_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.label_sonuc.setGeometry(QtCore.QRect(410, 90, 271, 81))
        self.label_sonuc.setStyleSheet("#label_sonuc{background-color: rgb(255, 255, 127);}")
        self.label_sonuc.setText("")
        self.label_sonuc.setObjectName("label_sonuc")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
import resource_rc