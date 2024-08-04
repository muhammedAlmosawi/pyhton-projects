import socket
from threading import Thread

client_names = {}

def client_handling(connection, address):
    default_name = f"Client-{address[1]}"
    client_names[connection] = default_name
    print(f"Connection from {client_names[connection]}")    

    try:
        while True:
            data = connection.recv(1024)
            
            if not data:
                break
            
            the_client = client_names[connection]
            data_decode = data.decode("utf-8")
            
            print(f"From {the_client}: {str(data_decode)}")
            if data_decode.startswith("/"):
                commands(data_decode, connection)
            else:
                broadcast_message(data_decode, connection)

    except Exception as e:
        print(f"Error with {the_client}: {str(e)}")
        
    finally:
        if connection in client_names:
            the_client = client_names.pop(connection)
        print(f"Connection closed with {the_client}")    
        connection.close()

def broadcast_message(message, sender_connection):
    sender_name = client_names[sender_connection]
    for client in client_names:
        if client != sender_connection:
            try:
                client.send(f"from {sender_name}: {message}".encode("utf-8"))
            except Exception as e:
                print(f"Error sending to client: {str(e)}")
            except:
                client.close()
                if client in client_names:
                    del client_names[client]
    
def commands(command, connection):
    command_parts = command.split(" ", 1)
    command_name = command_parts[0]

    if command_name == "/name" and len(command_parts) > 1:
        set_client_name(command_parts[1], connection)

    elif command_name == "/list":
        list_clients(connection)

    else:
        print("unknown command please enter a valid command")

def set_client_name(name, connection):
    old_name = client_names[connection]
    client_names[connection] = name
    broadcast_message(f"{old_name} changed their name to {name}", connection)
    print(f"{old_name} changed their name to {name}")
    connection.send(f"your name has changed to {name}".encode("utf-8"))

def list_clients(connection):
    clients_list = ", ".join([name for name in client_names.values()])
    connection.send(f"connected clients: {clients_list}".encode("utf-8"))

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
