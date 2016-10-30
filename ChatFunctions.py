from socket import *
from ChatAppGUI import *
from ChatServerGUI import *
from ChatLoginGUI import *


server_color = (100, 100, 100)
self_color = (75, 75, 75)
partner_color = (100, 100, 100)


def qt_load_entry_client(chat_app, entry_text, color):
    if entry_text != '':
        chat_app.add_to_message_list(text=entry_text, color=color)


def qt_load_entry_server(chat_app, entry_text):
    if entry_text != '':
        chat_app.add_to_message_list(text=entry_text)
