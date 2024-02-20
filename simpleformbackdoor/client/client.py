import socket
from config import HOST, PORT


def create_client_socket():
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((HOST, PORT))
    return socket_client


def client_socket():
    return None
