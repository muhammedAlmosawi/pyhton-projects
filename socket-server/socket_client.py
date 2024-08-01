import socket
from threading import Thread

def receive_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
        except:
            break

def client_socket():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    receive_thread = Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    message = input(" -> ")

    while message.lower().strip() != "bye":
        client_socket.send(message.encode())

        message = input(" -> ")

    client_socket.close()

if __name__ == "__main__":
    client_socket()