from ChatFunctions import *
import threading


# Host Socket Setup
host = '127.0.0.1'
port = 8001

client_socket = socket(AF_INET, SOCK_STREAM)


# Mouse Events
def click_action():
    entry_text = chat_app.get_message()
    qt_load_entry(chat_app, "You: " + entry_text)
    chat_app.clear_message_box()
    client_socket.sendall(bytes("Partner: " + entry_text, "UTF-8"))


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(dialog, click_action=click_action)


def receive_data():
    try:
        client_socket.connect((host, port))
        qt_load_connection_info(chat_app, "Successfully connected!\n-------------------------------")
    except:
        qt_load_connection_info(chat_app, "Unable to connect.\n")
        return

    while 1:
        try:
            data = client_socket.recv(1024)
        except:
            qt_load_connection_info(chat_app, "The host has disconnected...\n")
            break

        if data != '':
            qt_load_entry(chat_app, data.decode("UTF-8"))
        else:
            qt_load_connection_info(chat_app, "The host has disconnected...\n")
            break


receivingThread = threading.Thread(target=receive_data, daemon=True)


if __name__ == '__main__':
    receivingThread.start()
    dialog.show()
    sys.exit(app.exec_())
