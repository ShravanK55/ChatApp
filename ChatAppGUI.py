import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QtChatApp import Ui_ChatApp


class ChatAppGUI(Ui_ChatApp):
    def __init__(self, dialog, click_action):
        Ui_ChatApp.__init__(self)
        self.setupUi(dialog)

        self.sendButton.clicked.connect(click_action)

    def get_message(self):
        return self.messageEntryBox.toPlainText()

    def clear_message_box(self):
        self.messageEntryBox.clear()

    def add_to_browser(self, text):
        self.textBrowser.insertPlainText(text + '\n')
