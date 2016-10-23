from socket import *
import tkinter
import re
import urllib
import threading


host = gethostname()
port = 8001
conn = ''

host_socket = socket(AF_INET, SOCK_STREAM)
host_socket.bind((host, port))

# GUI Management
window_title = "ChatApp - Host"
base_window = tkinter.Tk()
base_window.title(window_title)
base_window.geometry("400x500")
base_window.resizable(width=tkinter.FALSE, height=tkinter.FALSE)

chat_log = tkinter.Text(base_window, bd=0, bg="white", height="8", width="50", font="Arial")
chat_log.insert(tkinter.END, "Waiting for partner to connect...\n")
chat_log.config(state=tkinter.DISABLED)

scroll_bar = tkinter.Scrollbar(base_window, command=chat_log.yview, cursor="heart")
chat_log['yscrollcommand'] = scroll_bar.set

send_button = tkinter.Button(base_window, font=30, text="Send", width="12", height="5",
                             bd=0, bg="#FFBF00", activebackground="#FACC2E")  # command=ClickAction

entry_box = tkinter.Text(base_window, bd=0, bg="white", width="29", height="5", font="Arial")
#  entry_box.bind("<Return>", DisableEntry)
#  entry_box.bind("<KeyRelease-Return>", PressAction)

scroll_bar.place(x=376, y=6, height=386)
chat_log.place(x=6, y=6, height=386, width=370)
entry_box.place(x=128, y=401, height=90, width=265)
send_button.place(x=6, y=401, height=90)

base_window.mainloop()
