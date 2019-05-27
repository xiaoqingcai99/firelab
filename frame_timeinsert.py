# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeinsert.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_insert_time(object):
    def setupUi(self, insert_time):
        insert_time.setObjectName("insert_time")
        insert_time.resize(293, 216)
        self.label = QtWidgets.QLabel(insert_time)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(insert_time)
        self.label_2.setGeometry(QtCore.QRect(230, 40, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(insert_time)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(insert_time)
        self.spinBox.setGeometry(QtCore.QRect(140, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(insert_time)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.positionx = QtWidgets.QSpinBox(insert_time)
        self.positionx.setGeometry(QtCore.QRect(130, 110, 51, 31))
        self.positionx.setObjectName("positionx")
        self.positiony = QtWidgets.QSpinBox(insert_time)
        self.positiony.setGeometry(QtCore.QRect(200, 110, 51, 31))
        self.positiony.setObjectName("positiony")
        self.label_4 = QtWidgets.QLabel(insert_time)
        self.label_4.setGeometry(QtCore.QRect(180, 110, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(insert_time)
        QtCore.QMetaObject.connectSlotsByName(insert_time)

    def retranslateUi(self, insert_time):
        _translate = QtCore.QCoreApplication.translate
        insert_time.setWindowTitle(_translate("insert_time", "输入参数"))
        self.label.setText(_translate("insert_time", "时间长度："))
        self.label_2.setText(_translate("insert_time", "分钟"))
        self.pushButton.setText(_translate("insert_time", "OK"))
        self.label_3.setText(_translate("insert_time", "着火位置："))
        self.label_4.setText(_translate("insert_time", "，"))

