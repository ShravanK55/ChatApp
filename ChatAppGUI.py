import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from QtChatApp import Ui_ChatApp


class ChatAppGUI(Ui_ChatApp):
    def __init__(self, dialog, click_action):
        Ui_ChatApp.__init__(self)
        self.setupUi(dialog)

        self.sendButton.clicked.connect(click_action)
        self.nameItemMap = {}

    def get_message(self):
        return self.messageEntryBox.toPlainText()

    def clear_message_box(self):
        self.messageEntryBox.clear()

    def add_to_message_list(self, text, color):
        item_color = QtGui.QColor()
        item_color.setRgb(color[0], color[1], color[2])
        item = QtWidgets.QListWidgetItem(text)
        item.setBackground(QtGui.QBrush(item_color))
        self.messagesList.addItem(item)

    def add_to_name_list(self, name, color):
        item_color = QtGui.QColor()
        item_color.setRgb(color[0], color[1], color[2])
        item = QtWidgets.QListWidgetItem(name)
        item.setBackground(QtGui.QBrush(item_color))
        self.nameList.addItem(item)

        self.nameItemMap[name] = item

    def remove_from_name_list(self, name):
        self.nameList.takeItem(self.nameList.row(self.nameItemMap[name]))
        del self.nameItemMap[name]
