from ChatFunctions import *
import threading
import select
import json


# Host Socket Setup
host = '127.0.0.1'
port = 8001
name = ''
recv_buffer = 1024

# Client Socket Creation
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.settimeout(2)


# Message Structure
message = {'type': 'Client', 'name': name, 'content': '', 'action': 'None'}


# Mouse Events
def connect_click_action():
    global host, port, name
    host = login_app.get_host()
    port = login_app.get_port()
    name = login_app.get_name()

    message['name'] = name
    message['content'] = name
    message['action'] = 'CheckName'

    # We use a temporary connection to check if our entered username is taken or not.
    # Also used to check if the connectivity to a host is proper or not.
    temp_socket = socket(AF_INET, SOCK_STREAM)
    temp_socket.settimeout(2)

    try:
        temp_socket.connect((host, port))
    except error:
        login_app.show_error("Could not connect to this host and address.")
        return

    message_to_send = json.dumps(message)
    temp_socket.send(bytes(message_to_send, "UTF-8"))

    # Checks if the entered username is already taken by the another client.
    try:
        data = temp_socket.recv(recv_buffer)
        if not data:
            login_app.show_error("Could not connect to the server!")
            sys.exit()
        else:
            result = data.decode("UTF-8")
            if result == "Taken":
                login_app.show_error("This user name is taken. Please use another one.")
                return
    except error:
        login_app.show_error("Could not connect to the server!")
        sys.exit()

    # Once the temporary connection succeeds/fails, we disconnect.
    try:
        message['action'] = 'TempDisconnect'
        message_to_send = json.dumps(message)
        temp_socket.send(bytes(message_to_send, "UTF-8"))
    except error:
        login_app.show_error("Error in connecting to the server.")
        sys.exit()

    temp_socket.close()

    login_dialog.close()
    chat_dialog.show()
    client_thread.start()


# Sends the entered message to the server, and clears the entry box.
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


# Sends a message to the server, in order to retrieve all users currently connected to the chat room.
def connect_message():
    message['name'] = name
    message['action'] = 'UpdateName'
    message_to_send = json.dumps(message)
    client_socket.send(bytes(message_to_send, "UTF-8"))


# GUI Creation
app = QtWidgets.QApplication(sys.argv)
login_dialog = QtWidgets.QDialog()
login_app = ChatLoginGUI(login_dialog, click_action=connect_click_action)
chat_dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(chat_dialog, click_action=send_click_action)


# Function to create the client socket and run it, and is called by the client thread.
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

        # Checks which sockets have messages to read, which sockets are attempting to connect, errors.
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        for sock in ready_to_read:
            if sock == client_socket:
                try:
                    data = sock.recv(recv_buffer)
                    # If a message arrives with no data, it means that the client has been disconnected from the server.
                    if not data:
                        qt_load_entry_client(chat_app, "Disconnected from chat server!", color=server_color)
                        sys.exit()
                    else:
                        handle_message(data)

                except error:
                    qt_load_entry_client(chat_app, "Disconnected from chat server!", color=server_color)
                    sys.exit()


# Handles the received message.
def handle_message(msg):
    global name
    received_message = json.loads(msg.decode("UTF-8"))

    # A message from another client.
    if received_message['type'] == 'Client':
        qt_load_entry_client(chat_app, received_message['name'] + ": "
                             + received_message['content'], color=partner_color)

    # A message from the server.
    elif received_message['type'] == 'Server':
        # Message received when the user/other users are connected.
        if received_message['action'] == 'Connected':
            # User has successfully connected.
            if received_message['name'] == name:
                names = json.loads(received_message['extra'])

                # Adds all connected users to the name list.
                for n in names:
                    qt_add_name(chat_app, name=n)

            # Another user has connected.
            else:
                if received_message['name'] != '':
                    qt_add_name(chat_app, name=received_message['name'])
                    qt_load_entry_client(chat_app, received_message['content'], color=server_color)

        # A user has disconnected from the chat room.
        elif received_message['action'] == 'Disconnected':
            if received_message['name'] != '':
                qt_remove_name(chat_app, name=received_message['name'])
                qt_load_entry_client(chat_app, received_message['content'], color=server_color)


client_thread = threading.Thread(target=chat_client, daemon=True)


if __name__ == '__main__':
    login_dialog.show()
    sys.exit(app.exec_())
