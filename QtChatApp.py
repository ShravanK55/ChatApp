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
        self.sendButton = QtWidgets.QPushButton(ChatApp)
        self.sendButton.setGeometry(QtCore.QRect(490, 390, 131, 71))
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.messageEntryBox = QtWidgets.QPlainTextEdit(ChatApp)
        self.messageEntryBox.setGeometry(QtCore.QRect(20, 390, 451, 71))
        self.messageEntryBox.setObjectName("messageEntryBox")
        self.textBrowser = QtWidgets.QTextBrowser(ChatApp)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 601, 351))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(ChatApp)
        QtCore.QMetaObject.connectSlotsByName(ChatApp)

    def retranslateUi(self, ChatApp):
        _translate = QtCore.QCoreApplication.translate
        ChatApp.setWindowTitle(_translate("ChatApp", "ChatApp"))
        self.sendButton.setText(_translate("ChatApp", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatApp = QtWidgets.QDialog()
    ui = Ui_ChatApp()
    ui.setupUi(ChatApp)
    ChatApp.show()
    sys.exit(app.exec_())

