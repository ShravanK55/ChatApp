# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtChatCreateServer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatApp(object):
    def setupUi(self, ChatApp):
        ChatApp.setObjectName("ChatApp")
        ChatApp.resize(320, 240)
        self.title = QtWidgets.QLabel(ChatApp)
        self.title.setGeometry(QtCore.QRect(100, 10, 120, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(43, 43, 43);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.createButton = QtWidgets.QPushButton(ChatApp)
        self.createButton.setGeometry(QtCore.QRect(120, 170, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.createButton.setObjectName("createButton")
        self.portLabel = QtWidgets.QLabel(ChatApp)
        self.portLabel.setGeometry(QtCore.QRect(40, 110, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portLabel.setFont(font)
        self.portLabel.setStyleSheet("color: rgb(43, 43, 43);")
        self.portLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portLabel.setObjectName("portLabel")
        self.ipEntry = QtWidgets.QLineEdit(ChatApp)
        self.ipEntry.setGeometry(QtCore.QRect(90, 78, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        self.ipEntry.setFont(font)
        self.ipEntry.setStyleSheet("color: rgb(43, 43, 43);")
        self.ipEntry.setObjectName("ipEntry")
        self.portEntry = QtWidgets.QLineEdit(ChatApp)
        self.portEntry.setGeometry(QtCore.QRect(90, 108, 190, 20))
        self.portEntry.setStyleSheet("color: rgb(43, 43, 43);")
        self.portEntry.setObjectName("portEntry")
        self.ipLabel = QtWidgets.QLabel(ChatApp)
        self.ipLabel.setGeometry(QtCore.QRect(40, 80, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ipLabel.setFont(font)
        self.ipLabel.setStyleSheet("color: rgb(43, 43, 43);")
        self.ipLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ipLabel.setObjectName("ipLabel")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp - Create Server"))
        self.title.setText(_translate("ChatApp", "Create Server"))
        self.createButton.setText(_translate("ChatApp", "Create"))
        self.portLabel.setText(_translate("ChatApp", "Port:"))
        self.ipEntry.setText(_translate("ChatApp", "127.0.0.1"))
        self.portEntry.setText(_translate("ChatApp", "8001"))
        self.ipLabel.setText(_translate("ChatApp", "IP:"))

