from ChatFunctions import *
import threading


# Host Socket Setup
host = '127.0.0.1'
port = 8001

client_socket = socket(AF_INET, SOCK_STREAM)


# Mouse Events
def click_action():
    entry_text = entry_box.get("0.0", tkinter.END)
    load_user_entry(chat_log, entry_text)
    chat_log.yview(tkinter.END)
    entry_box.delete("0.0", tkinter.END)
    client_socket.sendall(bytes(entry_text, "UTF-8"))


# Keyboard Events
def press_action(event):
    entry_box.config(state=tkinter.NORMAL)
    click_action()


def disable_entry(event):
    entry_box.config(state=tkinter.DISABLED)


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
                             bd=0, bg="#FFBF00", activebackground="#FACC2E", command=click_action)

entry_box = tkinter.Text(base_window, bd=0, bg="white", width="29", height="5", font="Arial")
entry_box.bind("<Return>", disable_entry)
entry_box.bind("<KeyRelease-Return>", press_action)

scroll_bar.place(x=376, y=6, height=386)
chat_log.place(x=6, y=6, height=386, width=370)
entry_box.place(x=128, y=401, height=90, width=265)
send_button.place(x=6, y=401, height=90)


def receive_data():
    try:
        client_socket.connect((host, port))
        load_connection_info(chat_log, "Successfully connected!\n-------------------------------")
    except:
        load_connection_info(chat_log, "Unable to connect.\n")
        return

    while 1:
        try:
            data = client_socket.recv(1024)
        except:
            load_connection_info(chat_log, "The host has disconnected...\n")
            break

        if data != '':
            load_partner_entry(chat_log, data.decode("UTF-8"))
        else:
            load_connection_info(chat_log, "The host has disconnected...\n")
            break


threading._start_new_thread(receive_data, ())

base_window.mainloop()  # Main window loop
