import socket
from threading import Thread

clients = []

def client_handling(connection, address):
    print(f"Connection from {str(address)}")
    clients.append(connection)

    try:
        while True:
            data = connection.recv(1024).decode()
            if not data:
                break

            print(f"From {str(address)}: {str(data)}")
            broadcast_message(data, connection)

    except Exception as e:
        print(f"Error with {str(address)}: {str(e)}")
        
    finally:    
        connection.close()
        if connection in clients:
            clients.remove(connection)
        print(f"Connection closed with {str(address)}")

def broadcast_message(message, sender_connection):
    for client in clients:
        if client != sender_connection:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error sending to client: {str(e)}")
            except:
                client.close()
                clients.remove(client)
    

def server_socket():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(4)
    
    print(f"server listening on {host}:{port}")

    while True:
        connection, address = server_socket.accept()
        client = Thread(target=client_handling, args=(connection, address))
        client.start()

if __name__ == "__main__":
    server_socket()