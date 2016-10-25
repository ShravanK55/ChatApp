from socket import *
from ChatAppGUI import *


def qt_load_connection_info(chat_app, entry_text):
    if entry_text != '':
        chat_app.add_to_browser(entry_text)


def qt_load_entry(chat_app, entry_text):
    if entry_text != '':
        chat_app.add_to_browser(entry_text)
