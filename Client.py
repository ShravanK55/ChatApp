from ChatFunctions import *
import threading
import select


# Host Socket Setup
host = '127.0.0.1'
port = 8001
recv_buffer = 1024

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(2)


# Mouse Events
def click_action():
    entry_text = chat_app.get_message()
    qt_load_entry(chat_app, "You: " + entry_text, color=self_color)
    chat_app.clear_message_box()
    client_socket.send(bytes(entry_text, "UTF-8"))


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(dialog, click_action=click_action)


def chat_client():
    try:
        client_socket.connect((host, port))
    except:
        qt_load_entry(chat_app, "Unable to connect!", color=server_color)
        sys.exit()

    qt_load_entry(chat_app, "Connected to chat room! You may now send messages.", color=server_color)

    while 1:
        socket_list = [client_socket]

        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        for sock in ready_to_read:
            if sock == client_socket:
                data = sock.recv(recv_buffer)
                if not data:
                    qt_load_entry(chat_app, "Disconnected from chat server!", color=server_color)
                    sys.exit()
                else:
                    qt_load_entry(chat_app, data.decode("UTF-8"), color=partner_color)


client_thread = threading.Thread(target=chat_client, daemon=True)


if __name__ == '__main__':
    client_thread.start()
    dialog.show()
    sys.exit(app.exec_())
