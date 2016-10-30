# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtChatLogin.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatApp(object):
    def setupUi(self, ChatApp):
        ChatApp.setObjectName("ChatApp")
        ChatApp.resize(320, 240)
        ChatApp.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.title = QtWidgets.QLabel(ChatApp)
        self.title.setGeometry(QtCore.QRect(135, 15, 50, 40))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(223, 223, 223);")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.hostLabel = QtWidgets.QLabel(ChatApp)
        self.hostLabel.setGeometry(QtCore.QRect(40, 80, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hostLabel.setFont(font)
        self.hostLabel.setStyleSheet("color: rgb(223, 223, 223);")
        self.hostLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hostLabel.setObjectName("hostLabel")
        self.portLabel = QtWidgets.QLabel(ChatApp)
        self.portLabel.setGeometry(QtCore.QRect(40, 110, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.portLabel.setFont(font)
        self.portLabel.setStyleSheet("color: rgb(223, 223, 223);")
        self.portLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portLabel.setObjectName("portLabel")
        self.nameLabel = QtWidgets.QLabel(ChatApp)
        self.nameLabel.setGeometry(QtCore.QRect(40, 140, 45, 15))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color: rgb(223, 223, 223);")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.connectButton = QtWidgets.QPushButton(ChatApp)
        self.connectButton.setGeometry(QtCore.QRect(120, 185, 80, 31))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.connectButton.setFont(font)
        self.connectButton.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.connectButton.setObjectName("connectButton")
        self.hostEntry = QtWidgets.QLineEdit(ChatApp)
        self.hostEntry.setGeometry(QtCore.QRect(90, 78, 190, 20))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        self.hostEntry.setFont(font)
        self.hostEntry.setStyleSheet("color: rgb(223, 223, 223);")
        self.hostEntry.setObjectName("hostEntry")
        self.portEntry = QtWidgets.QLineEdit(ChatApp)
        self.portEntry.setGeometry(QtCore.QRect(90, 108, 190, 20))
        self.portEntry.setStyleSheet("color: rgb(223, 223, 223);")
        self.portEntry.setObjectName("portEntry")
        self.nameEntry = QtWidgets.QLineEdit(ChatApp)
        self.nameEntry.setGeometry(QtCore.QRect(90, 138, 190, 20))
        self.nameEntry.setStyleSheet("color: rgb(223, 223, 223);")
        self.nameEntry.setObjectName("nameEntry")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp - Login"))
        self.title.setText(_translate("ChatApp", "Login"))
        self.hostLabel.setText(_translate("ChatApp", "Host:"))
        self.portLabel.setText(_translate("ChatApp", "Port:"))
        self.nameLabel.setText(_translate("ChatApp", "Name:"))
        self.connectButton.setText(_translate("ChatApp", "Connect"))
        self.hostEntry.setText(_translate("ChatApp", "127.0.0.1"))
        self.portEntry.setText(_translate("ChatApp", "8001"))
        self.nameEntry.setText(_translate("ChatApp", "User"))

