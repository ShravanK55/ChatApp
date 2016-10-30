# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtChatServer.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatApp(object):
    def setupUi(self, ChatApp):
        ChatApp.setObjectName("ChatApp")
        ChatApp.resize(640, 480)
        self.messagesList = QtWidgets.QListWidget(ChatApp)
        self.messagesList.setGeometry(QtCore.QRect(20, 50, 601, 411))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(12)
        self.messagesList.setFont(font)
        self.messagesList.setObjectName("messagesList")
        self.title = QtWidgets.QLabel(ChatApp)
        self.title.setGeometry(QtCore.QRect(265, 10, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp - Server"))
        self.title.setText(_translate("ChatApp", "Chat Server"))

