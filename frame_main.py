# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainmenu(object):
    def setupUi(self, mainmenu):
        mainmenu.setObjectName("mainmenu")
        mainmenu.resize(578, 318)
        self.centralwidget = QtWidgets.QWidget(mainmenu)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 441, 111))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setToolTipDuration(0)
        self.label.setObjectName("label")
        self.logon = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.logon.setGeometry(QtCore.QRect(230, 180, 111, 41))
        self.logon.setObjectName("logon")
        mainmenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainmenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainmenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainmenu)
        self.statusbar.setObjectName("statusbar")
        mainmenu.setStatusBar(self.statusbar)
        self.actionexit = QtWidgets.QAction(mainmenu)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainmenu)
        QtCore.QMetaObject.connectSlotsByName(mainmenu)

    def retranslateUi(self, mainmenu):
        _translate = QtCore.QCoreApplication.translate
        mainmenu.setWindowTitle(_translate("mainmenu", "林火蔓延预测软件"))
        self.label.setText(_translate("mainmenu", "欢迎使用林火蔓延预测软件"))
        self.logon.setText(_translate("mainmenu", "用户登录"))
        self.menu.setTitle(_translate("mainmenu", "菜单"))
        self.actionexit.setText(_translate("mainmenu", "exit"))

