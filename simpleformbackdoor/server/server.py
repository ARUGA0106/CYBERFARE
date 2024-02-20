import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('ascii')
        if not data:
            break
        print(f"Received from client: {data}")

    client_socket.close()

def start_server():
    HOST = "192.168.205.232"
    PORT = 9988

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
