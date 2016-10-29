# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtChatApp.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatApp(object):
    def setupUi(self, ChatApp):
        ChatApp.setObjectName("ChatApp")
        ChatApp.resize(640, 480)
        ChatApp.setAutoFillBackground(False)
        ChatApp.setStyleSheet("background-color: rgb(22, 22, 22);")
        self.sendButton = QtWidgets.QPushButton(ChatApp)
        self.sendButton.setEnabled(True)
        self.sendButton.setGeometry(QtCore.QRect(540, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.sendButton.setFont(font)
        self.sendButton.setAutoFillBackground(False)
        self.sendButton.setStyleSheet("background-image: url(:/Icons/SendButton.png);\n"
"border: none;")
        self.sendButton.setText("")
        self.sendButton.setObjectName("sendButton")
        self.messageEntryBox = QtWidgets.QPlainTextEdit(ChatApp)
        self.messageEntryBox.setGeometry(QtCore.QRect(20, 380, 501, 81))
        self.messageEntryBox.setStyleSheet("background-color: rgb(230, 255, 244);")
        self.messageEntryBox.setObjectName("messageEntryBox")
        self.messagesList = QtWidgets.QListWidget(ChatApp)
        self.messagesList.setGeometry(QtCore.QRect(20, 20, 591, 341))
        self.messagesList.setStyleSheet("background-color: rgb(230, 255, 244);")
        self.messagesList.setObjectName("messagesList")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp"))

import ChatAppResources_rc
