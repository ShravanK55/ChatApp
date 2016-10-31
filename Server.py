from ChatFunctions import *
import threading
import select
import json


# Host Socket Setup
host = '127.0.0.1'
port = 8001
recv_buffer = 1024
max_connections = 10
socket_list = []
name_table = {}

message = {'type': 'Server', 'name': 'Server', 'content': '', 'action': 'None', 'extra': ''}


# Mouse Events
def create_click_action():
    global host, port
    host = create_app.get_ip()
    port = create_app.get_port()

    create_server_dialog.close()
    server_dialog.show()
    server_thread.start()


app = QtWidgets.QApplication(sys.argv)
create_server_dialog = QtWidgets.QDialog()
create_app = ChatCreateServerGUI(create_server_dialog, click_action=create_click_action)
server_dialog = QtWidgets.QDialog()
chat_app = ChatServerGUI(server_dialog)


def chat_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(max_connections)

    socket_list.append(server_socket)

    qt_load_entry_server(chat_app, "Server started on port " + str(port))

    while 1:
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        for sock in ready_to_read:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                socket_list.append(sockfd)
                name_table[sockfd] = ''
                qt_load_entry_server(chat_app, "Client (%s, %s) attempting connection..." % addr)

            else:
                try:
                    data = sock.recv(recv_buffer)
                    if data:
                        handle_message(server_socket, sock, data)
                    else:
                        if sock in socket_list:
                            socket_list.remove(sock)
                            qt_load_entry_server(chat_app, str(sock.getpeername()) + " disconnected!")

                        message['name'] = name_table[sock]
                        message['action'] = 'Disconnected'
                        message['content'] = name_table[sock] + " has left the chat room!"
                        broadcast(server_socket, sock, message)
                        del name_table[sock]

                except error:
                    if sock in socket_list:
                        socket_list.remove(sock)
                        qt_load_entry_server(chat_app, str(sock.getpeername()) + " disconnected!")

                    message['name'] = name_table[sock]
                    message['action'] = 'Disconnected'
                    message['content'] = name_table[sock] + " has left the chat room!"
                    broadcast(server_socket, sock, message)
                    del name_table[sock]

    server_socket.close()


def handle_message(server_socket, sock, msg):
    received_message = json.loads(msg.decode("UTF-8"))
    if received_message['type'] == 'Client':
        if received_message['action'] == 'UpdateName' and sock != server_socket:
            name_table[sock] = received_message['name']
            qt_load_entry_server(chat_app, str(sock.getpeername()) + ": " + name_table[sock] + " has now connected!")

            message['name'] = received_message['name']
            message['action'] = 'Connected'
            message['content'] = '%s has entered the chat room!' % received_message['name']

            names = []
            for sockfd in socket_list:
                if sockfd != sock and sockfd != server_socket:
                    names.append(name_table[sockfd])
            names_to_send = json.dumps(names)
            message['extra'] = names_to_send

            broadcast_with_names(server_socket, sock, message)

        elif received_message['action'] == 'ClientMessage':
            broadcast(server_socket, sock, received_message)

        elif received_message['action'] == 'CheckName':
            for sockfd in name_table:
                if name_table[sockfd] == received_message['content']:
                    sock.send(bytes("Taken", "UTF-8"))
            sock.send(bytes("Available", "UTF-8"))

        elif received_message['action'] == 'TempDisconnect':
            if sock in socket_list:
                socket_list.remove(sock)


def broadcast(server_socket, sock, msg):
    for sockfd in socket_list:
        if sockfd != server_socket and sockfd != sock:
            try:
                message_to_send = json.dumps(msg)
                sockfd.send(bytes(message_to_send, "UTF-8"))
            except error:
                sockfd.close()
                if sockfd in socket_list:
                    socket_list.remove(sockfd)
                    del name_table[sockfd]


def broadcast_with_names(server_socket, sock, msg):
    for sockfd in socket_list:
        if sockfd != server_socket and sockfd != sock:
            try:
                message_to_send = json.dumps(msg)
                sockfd.send(bytes(message_to_send, "UTF-8"))
            except error:
                sockfd.close()
                if sockfd in socket_list:
                    socket_list.remove(sockfd)
                    del name_table[sockfd]
        elif sockfd != server_socket and sockfd == sock:
            try:
                message_to_send = json.dumps(msg)
                sockfd.send(bytes(message_to_send, "UTF-8"))
            except error:
                sockfd.close()
                if sockfd in socket_list:
                    socket_list.remove(sockfd)
                    del name_table[sockfd]


server_thread = threading.Thread(target=chat_server, daemon=True)


if __name__ == '__main__':
    create_server_dialog.show()
    sys.exit(app.exec_())
