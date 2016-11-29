from socket import *
from ChatAppGUI import *
from ChatServerGUI import *
from ChatLoginGUI import *
from ChatCreateServerGUI import *


server_color = (100, 100, 100)
self_color = (75, 75, 75)
partner_color = (100, 100, 100)
name_color = (100, 100, 100)


# Loads an entry onto the client's message list.
def qt_load_entry_client(chat_app, entry_text, color):
    if entry_text != '':
        chat_app.add_to_message_list(text=entry_text, color=color)


# Loads an entry onto the server's message list.
def qt_load_entry_server(chat_app, entry_text):
    if entry_text != '':
        chat_app.add_to_message_list(text=entry_text)


# Loads an entry onto a client's name list.
def qt_add_name(chat_app, name):
    if name != '':
        chat_app.add_to_name_list(name=name, color=name_color)


# Removes an entry from the client's name list.
def qt_remove_name(chat_app, name):
    if name != '':
        chat_app.remove_from_name_list(name=name)
