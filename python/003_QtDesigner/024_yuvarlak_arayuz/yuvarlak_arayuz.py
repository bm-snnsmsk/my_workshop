# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yuvarlak_arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/soccer_ball.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{\n"
"border-image: url(:/img/soccer_ball.ico);}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minimize.setStyleSheet("#pushButton_minimize{background-color: rgba(255, 255, 255,0);}")
        self.pushButton_minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/minimize.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minimize.setIcon(icon1)
        self.pushButton_minimize.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_minimize.setObjectName("pushButton_minimize")
        self.horizontalLayout.addWidget(self.pushButton_minimize)
        self.pushButton_full_screen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_full_screen.setStyleSheet("#pushButton_full_screen{background-color: rgba(255, 255, 255,0);}")
        self.pushButton_full_screen.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/maximize.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_full_screen.setIcon(icon2)
        self.pushButton_full_screen.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_full_screen.setObjectName("pushButton_full_screen")
        self.horizontalLayout.addWidget(self.pushButton_full_screen)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setStyleSheet("#pushButton_close{background-color: rgba(255, 255, 255,0);}")
        self.pushButton_close.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon3)
        self.pushButton_close.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 327, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yuvarlak Arayüz"))
import close_rc
import hello_rc
import home_2_rc
import login_rc
import maximize_rc
import minimize_rc
import soccer_ball_rc
import uc_rc