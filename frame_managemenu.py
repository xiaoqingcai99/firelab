# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managemenu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_manawindow(object):
    def setupUi(self, manawindow):
        manawindow.setObjectName("manawindow")
        manawindow.resize(1150, 616)
        self.centralwidget = QtWidgets.QWidget(manawindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 801, 551))
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 771, 521))
        self.tableView.setObjectName("tableView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(820, 10, 311, 551))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.insert = QtWidgets.QPushButton(self.groupBox_2)
        self.insert.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.insert.setObjectName("insert")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(30, 70, 271, 461))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.exit = QtWidgets.QPushButton(self.groupBox_2)
        self.exit.setGeometry(QtCore.QRect(220, 30, 75, 23))
        self.exit.setObjectName("exit")
        self.reset = QtWidgets.QPushButton(self.groupBox_2)
        self.reset.setGeometry(QtCore.QRect(130, 30, 75, 23))
        self.reset.setObjectName("reset")
        manawindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(manawindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1150, 23))
        self.menubar.setObjectName("menubar")
        manawindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(manawindow)
        self.statusbar.setObjectName("statusbar")
        manawindow.setStatusBar(self.statusbar)

        self.retranslateUi(manawindow)
        QtCore.QMetaObject.connectSlotsByName(manawindow)

    def retranslateUi(self, manawindow):
        _translate = QtCore.QCoreApplication.translate
        manawindow.setWindowTitle(_translate("manawindow", "林火蔓延预测软件"))
        self.groupBox.setTitle(_translate("manawindow", "演示效果"))
        self.insert.setText(_translate("manawindow", "输入参数"))
        self.exit.setText(_translate("manawindow", "退出"))
        self.reset.setText(_translate("manawindow", "重置"))

