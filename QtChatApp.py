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
        self.messagesList = QtWidgets.QListWidget(ChatApp)
        self.messagesList.setGeometry(QtCore.QRect(20, 20, 421, 341))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(11)
        self.messagesList.setFont(font)
        self.messagesList.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(220, 220, 220);")
        self.messagesList.setObjectName("messagesList")
        self.messageEntryBox = QtWidgets.QTextEdit(ChatApp)
        self.messageEntryBox.setGeometry(QtCore.QRect(20, 380, 500, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.messageEntryBox.setFont(font)
        self.messageEntryBox.setToolTip("")
        self.messageEntryBox.setToolTipDuration(-1)
        self.messageEntryBox.setStatusTip("")
        self.messageEntryBox.setWhatsThis("")
        self.messageEntryBox.setStyleSheet("color: rgb(232, 232, 232);")
        self.messageEntryBox.setObjectName("messageEntryBox")
        self.nameList = QtWidgets.QListWidget(ChatApp)
        self.nameList.setGeometry(QtCore.QRect(460, 20, 160, 340))
        self.nameList.setStyleSheet("background-color: rgb(77, 77, 77);\n"
"color: rgb(220, 220, 220);")
        self.nameList.setObjectName("nameList")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp - Client"))
        self.messageEntryBox.setHtml(_translate("ChatApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.messageEntryBox.setPlaceholderText(_translate("ChatApp", "Enter a message..."))

import ChatAppResources_rc
