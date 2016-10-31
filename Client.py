from ChatFunctions import *
import threading
import select
import json


# Host Socket Setup
host = '127.0.0.1'
port = 8001
name = 'User'
recv_buffer = 1024

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(2)

message = {'type': 'Client', 'name': name, 'content': '', 'action': 'None'}


# Mouse Events
def connect_click_action():
    global host, port, name
    host = login_app.get_host()
    port = login_app.get_port()
    name = login_app.get_name()

    message['name'] = name

    login_dialog.close()
    chat_dialog.show()
    client_thread.start()


def send_click_action():
    entry_text = chat_app.get_message()
    if entry_text != '':
        qt_load_entry_client(chat_app, "You: " + entry_text, color=self_color)
        chat_app.clear_message_box()

        message['name'] = name
        message['action'] = 'ClientMessage'
        message['content'] = entry_text
        message_to_send = json.dumps(message)

        client_socket.send(bytes(message_to_send, "UTF-8"))


def connect_message():
    message['name'] = name
    message['action'] = 'UpdateName'
    message_to_send = json.dumps(message)
    client_socket.send(bytes(message_to_send, "UTF-8"))


app = QtWidgets.QApplication(sys.argv)
login_dialog = QtWidgets.QDialog()
login_app = ChatLoginGUI(login_dialog, click_action=connect_click_action)
chat_dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(chat_dialog, click_action=send_click_action)


def chat_client():
    try:
        client_socket.connect((host, port))
    except error:
        qt_load_entry_client(chat_app, "Unable to connect!", color=server_color)
        sys.exit()

    qt_load_entry_client(chat_app, "Connected to chat room! You may now send messages.", color=server_color)
    connect_message()
    qt_add_name(chat_app, name=name)

    while 1:
        socket_list = [client_socket]

        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        for sock in ready_to_read:
            if sock == client_socket:
                try:
                    data = sock.recv(recv_buffer)
                    if not data:
                        qt_load_entry_client(chat_app, "Disconnected from chat server!", color=server_color)
                        sys.exit()
                    else:
                        handle_message(data)

                except error:
                    qt_load_entry_client(chat_app, "Disconnected from chat server!", color=server_color)
                    sys.exit()


def handle_message(msg):
    global name
    received_message = json.loads(msg.decode("UTF-8"))

    if received_message['type'] == 'Client':
        qt_load_entry_client(chat_app, received_message['name'] + ": "
                             + received_message['content'], color=partner_color)
    elif received_message['type'] == 'Server':
        if received_message['action'] == 'Connected':
            if received_message['name'] == name:
                names = json.loads(received_message['extra'])
                for n in names:
                    qt_add_name(chat_app, name=n)
            else:
                qt_add_name(chat_app, name=received_message['name'])
                qt_load_entry_client(chat_app, received_message['content'], color=server_color)

        elif received_message['action'] == 'Disconnected':
            qt_remove_name(chat_app, name=received_message['name'])
            qt_load_entry_client(chat_app, received_message['content'], color=server_color)


client_thread = threading.Thread(target=chat_client, daemon=True)


if __name__ == '__main__':
    login_dialog.show()
    sys.exit(app.exec_())
