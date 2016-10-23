from socket import *
import tkinter
import re
import urllib


def load_user_entry(chat_log, entry_text):
    if entry_text != '':
        chat_log.config(state=tkinter.NORMAL)
        if chat_log.index('end') != None:
            line_number = float(chat_log.index('end')) - 1.0
            chat_log.insert(tkinter.END, "You: " + entry_text)
            chat_log.tag_add("You", line_number, line_number + 0.4)
            chat_log.tag_config("You", foreground="#FF8000", font=("Arial", 12, "bold"))
            chat_log.config(state=tkinter.DISABLED)
            chat_log.yview(tkinter.END)


def load_partner_entry(chat_log, entry_text):
    if entry_text != '':
        chat_log.config(state=tkinter.NORMAL)
        if chat_log.index('end') != None:
            try:
                line_number = float(chat_log.index('end')) - 1.0
            except:
                pass
            chat_log.insert(tkinter.END, "Partner: " + entry_text)
            chat_log.tag_add("Partner", line_number, line_number + 0.4)
            chat_log.tag_config("Partner", foreground="#FF8000", font=("Arial", 12, "bold"))
            chat_log.config(state=tkinter.DISABLED)
            chat_log.yview(tkinter.END)
