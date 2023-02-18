# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statusbar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 40, 401, 271))
        self.frame.setStyleSheet("border-image: url(:/icons/bir.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu_renkler = QtWidgets.QMenu(self.menubar)
        self.menu_renkler.setObjectName("menu_renkler")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBar.setFont(font)
        self.toolBar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.action_red = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/red.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_red.setIcon(icon)
        self.action_red.setObjectName("action_red")
        self.action_yellow = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/yellow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_yellow.setIcon(icon1)
        self.action_yellow.setObjectName("action_yellow")
        self.action_green = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/green.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_green.setIcon(icon2)
        self.action_green.setObjectName("action_green")
        self.action_blue = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/blue.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_blue.setIcon(icon3)
        self.action_blue.setObjectName("action_blue")
        self.action_black = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/black.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_black.setIcon(icon4)
        self.action_black.setObjectName("action_black")
        self.action_white = QtWidgets.QAction(MainWindow)
        self.action_white.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/white.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_white.setIcon(icon5)
        self.action_white.setObjectName("action_white")
        self.action_siyah_menu = QtWidgets.QAction(MainWindow)
        self.action_siyah_menu.setIcon(icon4)
        self.action_siyah_menu.setObjectName("action_siyah_menu")
        self.action_sari_menu = QtWidgets.QAction(MainWindow)
        self.action_sari_menu.setIcon(icon1)
        self.action_sari_menu.setObjectName("action_sari_menu")
        self.action_beyaz_menu = QtWidgets.QAction(MainWindow)
        self.action_beyaz_menu.setCheckable(True)
        self.action_beyaz_menu.setIcon(icon5)
        self.action_beyaz_menu.setObjectName("action_beyaz_menu")
        self.menu_renkler.addAction(self.action_siyah_menu)
        self.menu_renkler.addAction(self.action_sari_menu)
        self.menu_renkler.addAction(self.action_beyaz_menu)
        self.menubar.addAction(self.menu_renkler.menuAction())
        self.toolBar.addAction(self.action_red)
        self.toolBar.addAction(self.action_black)
        self.toolBar.addAction(self.action_blue)
        self.toolBar.addAction(self.action_green)
        self.toolBar.addAction(self.action_yellow)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_white)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_renkler.setTitle(_translate("MainWindow", "Renkler"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_red.setText(_translate("MainWindow", "red"))
        self.action_red.setToolTip(_translate("MainWindow", "kırmızı"))
        self.action_red.setShortcut(_translate("MainWindow", "Shift+R"))
        self.action_yellow.setText(_translate("MainWindow", "yellow"))
        self.action_yellow.setToolTip(_translate("MainWindow", "sarı"))
        self.action_yellow.setShortcut(_translate("MainWindow", "Shift+Y"))
        self.action_green.setText(_translate("MainWindow", "green"))
        self.action_green.setToolTip(_translate("MainWindow", "yeşil"))
        self.action_green.setShortcut(_translate("MainWindow", "Shift+G"))
        self.action_blue.setText(_translate("MainWindow", "blue"))
        self.action_blue.setToolTip(_translate("MainWindow", "mavi"))
        self.action_blue.setShortcut(_translate("MainWindow", "Shift+B"))
        self.action_black.setText(_translate("MainWindow", "black"))
        self.action_black.setToolTip(_translate("MainWindow", "siyah"))
        self.action_black.setShortcut(_translate("MainWindow", "Alt+Shift+B"))
        self.action_white.setText(_translate("MainWindow", "white"))
        self.action_white.setToolTip(_translate("MainWindow", "siyah"))
        self.action_white.setShortcut(_translate("MainWindow", "Shift+W"))
        self.action_siyah_menu.setText(_translate("MainWindow", "siyah"))
        self.action_siyah_menu.setShortcut(_translate("MainWindow", "Alt+Shift+B"))
        self.action_sari_menu.setText(_translate("MainWindow", "sarı"))
        self.action_sari_menu.setShortcut(_translate("MainWindow", "Shift+Y"))
        self.action_beyaz_menu.setText(_translate("MainWindow", "beyaz"))
        self.action_beyaz_menu.setShortcut(_translate("MainWindow", "Shift+B"))
import bir_rc
import black_rc
import blue_rc
import green_rc
import red_rc
import white_rc
import yellow_rc