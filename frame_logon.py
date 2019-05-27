# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logon.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_2(object):
    def setupUi(self, register_2):
        register_2.setObjectName("register_2")
        register_2.resize(334, 228)
        self.label = QtWidgets.QLabel(register_2)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(register_2)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.manaid = QtWidgets.QLineEdit(register_2)
        self.manaid.setGeometry(QtCore.QRect(130, 49, 131, 31))
        self.manaid.setObjectName("manaid")
        self.manapassword = QtWidgets.QLineEdit(register_2)
        self.manapassword.setGeometry(QtCore.QRect(130, 110, 131, 31))
        self.manapassword.setObjectName("manapassword")
        self.pushButton = QtWidgets.QPushButton(register_2)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(register_2)
        QtCore.QMetaObject.connectSlotsByName(register_2)

    def retranslateUi(self, register_2):
        _translate = QtCore.QCoreApplication.translate
        register_2.setWindowTitle(_translate("register_2", "登录"))
        self.label.setText(_translate("register_2", "账号"))
        self.label_2.setText(_translate("register_2", "密码"))
        self.pushButton.setText(_translate("register_2", "OK"))

