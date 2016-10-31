import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QtChatLogin import Ui_ChatApp


class ChatLoginGUI(Ui_ChatApp):
    def __init__(self, dialog, click_action):
        Ui_ChatApp.__init__(self)
        self.setupUi(dialog)

        self.connectButton.clicked.connect(click_action)
        self.errorLabel.hide()

    def get_host(self):
        return self.hostEntry.text()

    def get_port(self):
        return int(self.portEntry.text())

    def get_name(self):
        return self.nameEntry.text()

    def show_error(self, error):
        self.errorLabel.setText(error)
        self.errorLabel.show()
