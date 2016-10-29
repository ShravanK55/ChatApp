from ChatFunctions import *
import threading


# Host Socket Setup
host = '127.0.0.1'
port = 8001
conn = ''

host_socket = socket(AF_INET, SOCK_STREAM)
host_socket.bind((host, port))


# Mouse Events
def click_action():
    entry_text = chat_app.get_message()
    qt_load_entry(chat_app, "You: " + entry_text, color=self_color)
    chat_app.clear_message_box()
    conn.sendall(bytes("Partner: " + entry_text, "UTF-8"))


app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(dialog, click_action=click_action)


def get_connected():
    host_socket.listen(1)
    qt_load_entry(chat_app, "Waiting for partner to connect...", color=server_color)
    global conn
    conn, addr = host_socket.accept()
    qt_load_entry(chat_app, "Connected with: " + str(addr) + "\n-------------------------------", color=server_color)

    while 1:
        try:
            data = conn.recv(1024)
            qt_load_entry(chat_app, data.decode("UTF-8"), color=partner_color)

        except:
            qt_load_entry(chat_app, "Your partner has disconnected!", color=server_color)
            get_connected()

    conn.close()


connectionThread = threading.Thread(target=get_connected, daemon=True)


if __name__ == '__main__':
    connectionThread.start()
    dialog.show()
    sys.exit(app.exec_())
