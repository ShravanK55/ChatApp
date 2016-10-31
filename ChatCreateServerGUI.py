import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QtChatCreateServer import Ui_ChatApp


class ChatCreateServerGUI(Ui_ChatApp):
    def __init__(self, dialog, click_action):
        Ui_ChatApp.__init__(self)
        self.setupUi(dialog)

        self.createButton.clicked.connect(click_action)

    def get_ip(self):
        return self.ipEntry.text()

    def get_port(self):
        return int(self.portEntry.text())
