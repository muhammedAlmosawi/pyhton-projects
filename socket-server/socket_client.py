import socket
from threading import Thread

def receive_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            print(f"\r--> received from the server: {data}", end="")
            print("\n -> ", end=" ")
        except:
            break

def client_socket():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    receive_thread = Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()
    
    while True:
        message = input(" -> ")
        client_socket.send(message.encode("utf-8"))

        if message.strip() == "bye":
            break
        

    client_socket.close()

if __name__ == "__main__":
    client_socket()
