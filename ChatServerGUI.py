import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QtChatServer import Ui_ChatApp


class ChatServerGUI(Ui_ChatApp):
    def __init__(self, dialog):
        Ui_ChatApp.__init__(self)
        self.setupUi(dialog)

    def add_to_message_list(self, text):
        item = QtWidgets.QListWidgetItem(text)
        self.messagesList.addItem(item)
