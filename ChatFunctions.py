from socket import *
from ChatAppGUI import *


server_color = (250, 250, 250)
self_color = (225, 225, 225)
partner_color = (200, 200, 200)


def qt_load_entry(chat_app, entry_text, color):
    if entry_text != '':
        chat_app.add_to_message_list(text=entry_text, color=color)
