from ChatFunctions import *
import threading
import select


# Host Socket Setup
host = '127.0.0.1'
port = 8001
recv_buffer = 1024
max_connections = 10
socket_list = []


# Mouse Events
def click_action():
    return

app = QtWidgets.QApplication(sys.argv)
dialog = QtWidgets.QDialog()
chat_app = ChatAppGUI(dialog, click_action=click_action)


def chat_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(max_connections)

    socket_list.append(server_socket)

    qt_load_entry(chat_app, "Server started on port " + str(port), color=server_color)

    while 1:
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [], 0)

        for sock in ready_to_read:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                socket_list.append(sockfd)
                qt_load_entry(chat_app, "Client (%s, %s) connected!" % addr, color=server_color)
                broadcast(server_socket, sockfd, "[%s, %s] has entered the chat room!" % addr)

            else:
                try:
                    data = sock.recv(recv_buffer)
                    if data:
                        broadcast(server_socket, sock, "<" + str(sock.getpeername()) + "> " + data.decode("UTF-8"))
                    else:
                        if sock in socket_list:
                            socket_list.remove(sock)
                        qt_load_entry(chat_app, str(sock.getpeername()) + " disconnected!", color=server_color)
                        broadcast(server_socket, sock, str(sock.getpeername()) + " has left the chat room!")

                except:
                    if sock in socket_list:
                        socket_list.remove(sock)
                    qt_load_entry(chat_app, str(sock.getpeername()) + " disconnected!", color=server_color)
                    broadcast(server_socket, sock, str(sock.getpeername()) + " has left the chat room!")
                    continue

    server_socket.close()


def broadcast(server_socket, sock, message):
    for sockfd in socket_list:
        if sockfd != server_socket and sockfd != sock:
            try:
                sockfd.send(bytes(message, "UTF-8"))
            except:
                sockfd.close()
                if sockfd in socket_list:
                    socket_list.remove(sockfd)


server_thread = threading.Thread(target=chat_server, daemon=True)


if __name__ == '__main__':
    server_thread.start()
    dialog.show()
    sys.exit(app.exec_())
