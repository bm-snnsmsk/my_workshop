# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/bm_snnsmsk/Desktop/my_workspace/PROJELER/library_PYTHON/add_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 534)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/add_user.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#centralwidget{background-color: rgb(129, 205, 255);}\n"
"QPushButton{\n"
"background-color: rgb(242, 255, 157);\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(7)
        self.formLayout.setObjectName("formLayout")
        self.label_user_fist_name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_fist_name.setFont(font)
        self.label_user_fist_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_fist_name.setObjectName("label_user_fist_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_user_fist_name)
        self.lineEdit_user_first_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user_first_name.setFont(font)
        self.lineEdit_user_first_name.setText("")
        self.lineEdit_user_first_name.setObjectName("lineEdit_user_first_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user_first_name)
        self.label_user_fist_name_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_fist_name_2.setFont(font)
        self.label_user_fist_name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_fist_name_2.setObjectName("label_user_fist_name_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_user_fist_name_2)
        self.lineEdit_user_last_name = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user_last_name.setFont(font)
        self.lineEdit_user_last_name.setText("")
        self.lineEdit_user_last_name.setObjectName("lineEdit_user_last_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user_last_name)
        self.label_user_fist_name_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_fist_name_3.setFont(font)
        self.label_user_fist_name_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_fist_name_3.setObjectName("label_user_fist_name_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_user_fist_name_3)
        self.lineEdit_user_email = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user_email.setFont(font)
        self.lineEdit_user_email.setText("")
        self.lineEdit_user_email.setObjectName("lineEdit_user_email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user_email)
        self.lineEdit_user_telefon = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_user_telefon.setFont(font)
        self.lineEdit_user_telefon.setText("")
        self.lineEdit_user_telefon.setObjectName("lineEdit_user_telefon")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_user_telefon)
        self.label_user_fist_name_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_fist_name_5.setFont(font)
        self.label_user_fist_name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_fist_name_5.setObjectName("label_user_fist_name_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_user_fist_name_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_resim_ekle = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_resim_ekle.setFont(font)
        self.pushButton_resim_ekle.setObjectName("pushButton_resim_ekle")
        self.horizontalLayout.addWidget(self.pushButton_resim_ekle)
        self.label_user_resim = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_resim.setFont(font)
        self.label_user_resim.setText("")
        self.label_user_resim.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_resim.setObjectName("label_user_resim")
        self.horizontalLayout.addWidget(self.label_user_resim)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.pushButton_add_user = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_add_user.setFont(font)
        self.pushButton_add_user.setObjectName("pushButton_add_user")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pushButton_add_user)
        self.label_user_fist_name_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_user_fist_name_4.setFont(font)
        self.label_user_fist_name_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_user_fist_name_4.setObjectName("label_user_fist_name_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_user_fist_name_4)
        self.gridLayout.addLayout(self.formLayout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Üye Ekle"))
        self.label.setText(_translate("MainWindow", "Üye Ekle"))
        self.label_user_fist_name.setText(_translate("MainWindow", "Üye Adı"))
        self.label_user_fist_name_2.setText(_translate("MainWindow", "Üye Soyadı"))
        self.label_user_fist_name_3.setText(_translate("MainWindow", "Üye Email"))
        self.label_user_fist_name_5.setText(_translate("MainWindow", "Üye Resmi"))
        self.pushButton_resim_ekle.setText(_translate("MainWindow", "Resim Seç"))
        self.pushButton_add_user.setText(_translate("MainWindow", "Üye Ekle"))
        self.label_user_fist_name_4.setText(_translate("MainWindow", "Üye Telefon Numarası"))
import add_user_rc